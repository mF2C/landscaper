# Copyright (c) 2017, Intel Research and Development Ireland Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
DataClay Collector
"""
from os import path
import sys
from landscaper.collector import base
from landscaper.common import LOG
from landscaper import paths
from dataclay import api
api.init()

from dataclay.exceptions.exceptions import DataclayException
from model_mf2c.classes import *


CONFIG_SECTION_GENERAL = 'general'
CONFIG_VARIABLE_DC_AGENT = "dataclay_agentid"

CONFIG_SECTION_PHYSICAL = 'physical_layer'
CONFIG_VARIABLE_MACHINES = 'machines'

class DataClayCollector(base.Collector):
    """
    DataClay collector. Queries DataClay DB for hwloc and cpu_info files and
    saves files in the Data Directory.
    """
    def __init__(self, graph_db, conf_manager, events_manager, events=None):
        super(DataClayCollector, self).__init__(graph_db, conf_manager,
                                                events_manager, events=None)
        self.cnf = conf_manager

    def init_graph_db(self):
        """
        Retrieve hwloc and cpu_info for each machine and add
        files to the Data Directory.
        """
        LOG.info("Generating hwloc and cpu_info files")
        devices = list()

        # get dataClay agent_id
        agent_id = self.cnf.get_variable(CONFIG_SECTION_GENERAL, CONFIG_VARIABLE_DC_AGENT)
        if agent_id is None:
            LOG.error("'dataclay_agentid' has not been set in the 'general' section of the config file")
            return

        # get this device's agent
        this_agent = Agent.get_by_alias(agent_id)
        if self.generate_files(this_agent.device) :
            devices.append(this_agent.device.device_id)

        # get child devices - if leader
        if this_agent.is_leader:
            for child in this_agent.children:
                if self.generate_files(child.device):
                    devices.append(child.device.device_id)

        # write the device list to the config file
        device_list = ','.join(str(x) for x in devices)
        LOG.info("DataClay device list: " + device_list)
        self.conf_manager.set_variable(CONFIG_SECTION_PHYSICAL, CONFIG_VARIABLE_MACHINES, device_list)

        # cleanup
        api.finish()

    def update_graph_db(self, event, body):
        """
        Not implemented as there is no update events for DataClay.
        """
        raise NotImplementedError

    def generate_files(self, device):
        """
        Queries the hwloc and cpuinfo methods and writes them to a file
        :param device: model_mf2c.classes.Device used to query the hwloc and cpu_info methods
        :return: True if file successfully save, False if errors encountered
        """
        try:
            hwloc_path = path.join(paths.DATA_DIR, device.device_id + "_hwloc.xml")
            hwloc = device.get_hwloc()
            if hwloc is None:
                LOG.error("hwLoc data has not been set for this device: " + device.device_id + ". No HwLoc file will be saved.")
                return False
            self._write_to_file(hwloc_path, hwloc)

            cpu_path = path.join(paths.DATA_DIR, device.device_id + "_cpu_info.txt")
            cpu_info = device.get_CPU_info()
            if cpu_info is None:
                LOG.error("CPU_info data has not been set for this device: " + device.device_id + ". No CPU_info file will be saved.")
                return False
            self._write_to_file(cpu_path, cpu_info)
        except DataclayException as dc_ex:
            LOG.error("Error accessing hwloc/cpuinfo for device id: " + device.device_id + dc_ex.message)
            return False
        except:
            LOG.error("General Error hwloc/cpuinfo for device id: " + device.device_id, sys.exc_info()[0])
            return False
        return True

    @staticmethod
    def _write_to_file(filename, file_content):
        """
        Creates file, writes to file, saves  and closes file
        :param filename: file name including file path
        :param file_content: string content for file
        """
        file_handler = open(filename, "w")
        file_handler.write(file_content)
        file_handler.close()

if __name__ == "__main__":
    from landscaper.utilities import configuration
    conf_manager = configuration.ConfigurationManager()
    conf_manager.add_section('physical_layer')
    conf_manager.add_section('general')

    dut = DataClayCollector(None, conf_manager,None, None)
    dut.init_graph_db()
