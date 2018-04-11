# Automatically created by dataClay
import os
import sys

from dataclay import dclayMethod, dclayEmptyMethod, DataClayObject
from dataclay.contrib.dummy_pycompss import *

from logging import getLogger
getLogger('dataclay.deployed_classes').debug('Package path: ./demo/stubs/sources/model_mf2c/classes')
StorageObject = DataClayObject

###############################################################
######### <Class-based imports>:


######### </Class-based imports>
###############################################################

try:
    from pycompss.api.task import task
except ImportError:
    from dataclay.contrib.dummy_pycompss import *

# dataClay header
# This is a Stub, to be used for the user client
from dataclay import dclayMethod, DataClayObject

# Imports required by the following class

# Definition of dataClay object class: BehaviourInfo
class BehaviourInfo(DataClayObject):

    @dclayMethod(obj='anything', property_name='str', value='anything', beforeUpdate='str', afterUpdate='str')
    def __setUpdate__(self, obj, property_name, value, beforeUpdate, afterUpdate):
        if beforeUpdate is not None:
            getattr(self, beforeUpdate)(property_name, value)
        object.__setattr__(obj, "%s%s" % ("_dataclay_property_", property_name), value)
        if afterUpdate is not None:
            getattr(self, afterUpdate)(property_name, value)
    @dclayMethod(fields="list<str>", return_="dict")
    def _to_dict(self, fields):
        return {field: self.__getattribute__(field) for field in fields}
    @dclayMethod(return_="dict")
    def to_dict(self):
        fields = [
            "mobile",
            "reliability",
            "trust",
            "leader_capable"
        ]
        return self._to_dict(fields)
    @dclayMethod(mobile="bool", reliability="str", trust="str", leader_capable="bool")
    def __init__(self, mobile, reliability, trust, leader_capable):
        self.mobile = mobile
        self.reliability = reliability
        self.trust = trust
        self.leader_capable = leader_capable
    pass
# End of class definition
# dataClay header
# This is a Stub, to be used for the user client
from dataclay import dclayMethod, DataClayObject

# Imports required by the following class

# Definition of dataClay object class: NetworkInfo
class NetworkInfo(DataClayObject):

    @dclayMethod(io="str", eth_info="str", eth_address="str", wifi_info="str", wifi_address="str", bandwidth ="str", standard="str")
    def __init__(self, io, eth_info, eth_address, wifi_info, wifi_address, bandwidth, standard):
        self.network_io = io
        self.ethernet_info = eth_info
        self.ethernet_address = eth_address
        self.wifi_info = wifi_info
        self.wifi_address = wifi_address
        self.bandwidth_capacity = bandwidth
        self.standard_info = standard
    @dclayMethod(return_="dict")
    def to_dict(self):
        fields = [
            "network_io",
            "ethernet_info",
            "ethernet_address",
            "wifi_info",
            "wifi_address",
            "bandwidth_capacity",
            "standard_info"
        ]
        return self._to_dict(fields)
    @dclayMethod(obj='anything', property_name='str', value='anything', beforeUpdate='str', afterUpdate='str')
    def __setUpdate__(self, obj, property_name, value, beforeUpdate, afterUpdate):
        if beforeUpdate is not None:
            getattr(self, beforeUpdate)(property_name, value)
        object.__setattr__(obj, "%s%s" % ("_dataclay_property_", property_name), value)
        if afterUpdate is not None:
            getattr(self, afterUpdate)(property_name, value)
    @dclayMethod(fields="list<str>", return_="dict")
    def _to_dict(self, fields):
        return {field: self.__getattribute__(field) for field in fields}
    pass
# End of class definition
# dataClay header
# This is a Stub, to be used for the user client
from dataclay import dclayMethod, DataClayObject

# Imports required by the following class

# Definition of dataClay object class: Component
class Component(DataClayObject):

    @dclayMethod(obj='anything', property_name='str', value='anything', beforeUpdate='str', afterUpdate='str')
    def __setUpdate__(self, obj, property_name, value, beforeUpdate, afterUpdate):
        if beforeUpdate is not None:
            getattr(self, beforeUpdate)(property_name, value)
        object.__setattr__(obj, "%s%s" % ("_dataclay_property_", property_name), value)
        if afterUpdate is not None:
            getattr(self, afterUpdate)(property_name, value)
    @dclayMethod(sensor_type="str", actuator_type="str", comm_info="str", device_type="str", location="str")
    def __init__(self, sensor_type, actuator_type, comm_info, device_type, location):
        self.sensor_type = sensor_type
        self.actuator_type = actuator_type
        self.communication_info = comm_info
        self.device_type = device_type
        self.location = location
    @dclayMethod(other="model_mf2c.classes.Component", return_="bool")
    def __eq__(self, other):
        if not isinstance(other, Component):
            return False

        return all((
            self.sensor_type == other.sensor_type,
            self.actuator_type == other.actuator_type,
            self.communication_info == other.communication_info,
            self.device_type == other.device_type,
            self.location == other.location
        ))
    @dclayMethod(fields="list<str>", return_="dict")
    def _to_dict(self, fields):
        return {field: self.__getattribute__(field) for field in fields}
    @dclayMethod(return_="dict")
    def to_dict(self):
        fields = [
            "sensor_type",
            "actuator_type",
            "communication_info",
            "device_type",
            "location"
        ]
        return self._to_dict(fields)
    pass
# End of class definition
# dataClay header
# This is a Stub, to be used for the user client
from dataclay import dclayMethod, DataClayObject

# Imports required by the following class

# Definition of dataClay object class: Device
class Device(DataClayObject):

    @dclayMethod(return_="str")
    def get_CPU_info(self):
        return self.static_info.CPU_info
    @dclayMethod(hwloc="str")
    def set_hwloc(self, hwloc):
        self.static_info.hwloc = hwloc
    @dclayMethod(obj='anything', property_name='str', value='anything', beforeUpdate='str', afterUpdate='str')
    def __setUpdate__(self, obj, property_name, value, beforeUpdate, afterUpdate):
        if beforeUpdate is not None:
            getattr(self, beforeUpdate)(property_name, value)
        object.__setattr__(obj, "%s%s" % ("_dataclay_property_", property_name), value)
        if afterUpdate is not None:
            getattr(self, afterUpdate)(property_name, value)
    @dclayMethod(return_="str")
    def get_hwloc(self):
        return self.static_info.hwloc
    @dclayMethod(device_id="str", owner="model_mf2c.classes.User", static_info="model_mf2c.classes.StaticInfo", dynamic_info="model_mf2c.classes.DynamicInfo", network_info="model_mf2c.classes.NetworkInfo", behaviour_info="model_mf2c.classes.BehaviourInfo", security_info="model_mf2c.classes.SecurityInfo", attached_components="list<model_mf2c.classes.Component>", sharing_model_info="model_mf2c.classes.SharingModelInfo")
    def __init__(self, device_id, owner, static_info, dynamic_info, network_info, behaviour_info, security_info, attached_components, sharing_model_info):
        self.device_id = device_id
        self.owner = owner
        self.static_info = static_info
        self.dynamic_info = dynamic_info
        self.network_info = network_info
        self.behaviour_info = behaviour_info
        self.security_info = security_info
        self.attached_components = attached_components
        self.sharing_model_info = sharing_model_info
    @dclayMethod(cpu_info="str")
    def set_CPU_info(self, cpu_info):
        self.static_info.CPU_info = cpu_info
    pass
# End of class definition
# dataClay header
# This is a Stub, to be used for the user client
from dataclay import dclayMethod, DataClayObject

# Imports required by the following class

# Definition of dataClay object class: StaticInfo
class StaticInfo(DataClayObject):

    @dclayMethod(fields="list<str>", return_="dict")
    def _to_dict(self, fields):
        return {field: self.__getattribute__(field) for field in fields}
    @dclayMethod(return_="dict")
    def to_dict(self):
        fields = [
            "operating_system",
            "system_architecture",
            "processor_maker_name",
            "processor_architecture",
            "num_CPUs",
            "CPU_clock_speed",
            "total_num_cores",
            "total_RAM_size",
            "total_storage_size",
            "limited_power",
            "graphics_card_info"
        ]
        return self._to_dict(fields)
    @dclayMethod(os="str", arch="str", proc_maker="str", proc_arch="str", num_CPUs="int", CPU_speed="int", total_cores="int", RAM_size="int", storage_size="int", limited="bool", graphics_card="str")
    def __init__(self, os, arch, proc_maker, proc_arch, num_CPUs, CPU_speed, total_cores, RAM_size, storage_size, limited, graphics_card):
        self.operating_system = os
        self.system_architecture = arch
        self.processor_maker_name = proc_maker
        self.processor_architecture = proc_arch
        self.num_CPUs = num_CPUs
        self.CPU_clock_speed = CPU_speed
        self.total_num_cores = total_cores
        self.total_RAM_size = RAM_size
        self.total_storage_size = storage_size
        self.limited_power = limited
        self.graphics_card_info = graphics_card
        self.CPU_info = None
        self.hwloc = None
    @dclayMethod(obj='anything', property_name='str', value='anything', beforeUpdate='str', afterUpdate='str')
    def __setUpdate__(self, obj, property_name, value, beforeUpdate, afterUpdate):
        if beforeUpdate is not None:
            getattr(self, beforeUpdate)(property_name, value)
        object.__setattr__(obj, "%s%s" % ("_dataclay_property_", property_name), value)
        if afterUpdate is not None:
            getattr(self, afterUpdate)(property_name, value)
    pass
# End of class definition
# dataClay header
# This is a Stub, to be used for the user client
from dataclay import dclayMethod, DataClayObject

# Imports required by the following class

# Definition of dataClay object class: Agent
class Agent(DataClayObject):

    @dclayMethod(bw="int")
    def set_bandwidth_capacity(self, bw):
        self._check_cloud("Trying to set bandwidth capacity on a cloud agent")
        self.device.network_info.bandwidth_capacity = bw
    @dclayMethod(return_=None)
    def calculate_aggregation(self):
        """ Update own properties (to be defined) taking info from the agent (device, children, other aggregated info) """
        pass
    @dclayMethod(RAM="int")
    def set_shared_RAM_size(self, RAM):
        self._check_cloud("Trying to set shared RAM size on a cloud agent")
        self.device.sharing_model_info.shared_RAM_size = RAM
    @dclayMethod(return_=None, exception_message="str")
    def _check_cloud(self, exception_message):
        if self.is_cloud:
            raise RuntimeError(exception_message)
    @dclayMethod(address="str")
    def set_ethernet_address(self, address):
        self._check_cloud("Trying to set ethernet address on a cloud agent")
        self.device.network_info.ethernet_address = address
    @dclayMethod(return_="dict<str, dict>")
    def get_all_children_info(self):
        if self.is_leader or self.is_cloud:
            return {child.id: child.get_resource_info_as_dict() for child in self.children}
        else:
            raise RuntimeError("Trying to get children on a normal agent")
    @dclayMethod(info="str")
    def set_ethernet_info(self, info):
        self._check_cloud("Trying to set ethernet info on a cloud agent")
        self.device.network_info.ethernet_info = info
    @dclayMethod(info="str")
    def set_standard_info(self, info):
        self._check_cloud("Trying to set network standard info on a cloud agent")
        self.device.network_info.standard_info = info
    @dclayMethod(CPU="int")
    def set_shared_CPU_percent(self, CPU):
        self._check_cloud("Trying to set shared CPU percent on a cloud agent")
        self.device.sharing_model_info.shared_CPU_percent = CPU
    @dclayMethod(device_sec="bool")
    def set_device_security(self, device_sec):
        self._check_cloud("Trying to set device security on a cloud agent")
        self.device.security_info.device_security = device_sec
    @dclayMethod(multicloud="bool")
    def set_multicloud_federation(self, multicloud):
        self._check_cloud("Trying to set multicloud federation on a non-cloud agent")
        self.multicloud_federation = multicloud
    @dclayMethod(percent="int")
    def set_remaining_power_percent(self, percent):
        self._check_cloud("Trying to set remaining power percent on a cloud agent")
        self.device.dynamic_info.remaining_power_percent = percent
    @dclayMethod(component="model_mf2c.classes.Component")
    def add_attached_component(self, component):
        self._check_cloud("Trying to add an attached component to a cloud agent")
        self.device.attached_components.append(component)
    @dclayMethod(return_="list<model_mf2c.classes.Component>")
    def get_attached_component_info(self):
        self._check_cloud("Trying to get attached components on a cloud agent")
        return self.device.attached_components
    @dclayMethod(return_="bool")
    def get_multicloud_federation(self):
        self._check_cloud("Trying to get multicloud federation on a non-cloud agent")
        return self.multicloud_federation
    @dclayMethod(child="model_mf2c.classes.Agent")
    def remove_child(self, child):
        if self.is_leader or self.is_cloud:
            try:
                self.children.remove(child)
            except ValueError:
                pass
            self.aggregated_resource_info.calculate_aggregation()
        else:
            raise RuntimeError("Trying to remove a child from a normal agent")
    @dclayMethod(size="int")
    def set_available_RAM_size(self, size):
        self._check_cloud("Trying to set available RAM size on a cloud agent")
        self.device.dynamic_info.available_RAM_size = size
    @dclayMethod(io="str")
    def set_network_io(self, io):
        self._check_cloud("Trying to set network IO on a cloud agent")
        self.device.network_info.network_io = io
    @dclayMethod(size="int")
    def set_available_storage_size(self, size):
        self._check_cloud("Trying to set available storage size on a cloud agent")
        self.device.dynamic_info.available_storage_size = size
    @dclayMethod(child="model_mf2c.classes.Agent")
    def add_child(self, child):
        if self.is_leader or self.is_cloud:
            self.children.append(child)
            self.aggregated_resource_info.calculate_aggregation()
        else:
            raise RuntimeError("Trying to add a child to a normal agent")
    @dclayMethod(my_device="model_mf2c.classes.Device")
    def __init__(self, my_device):
        self.id = my_device.device_id #For the moment I assign the same id to the device and to the agent
        self.aggregated_resource_info = AggregatedResourceInfo(self) #AggregatedResourceInfo about the associated device
        self.device = my_device
        self.children = list()
        self.is_leader = False
        self.is_cloud = False
        self.multicloud_federation = False
    @dclayMethod(return_="list")
    def get_attached_component_info_as_list(self):
        self._check_cloud("Trying to get attached components on a cloud agent")
        ret = list()
        for comp in self.get_attached_component_info():
            ret.append(comp.to_dict())
        return ret
    @dclayMethod(beh_info="model_mf2c.classes.BehaviourInfo")
    def set_behaviour_info(self, beh_info):
        self._check_cloud("Trying to set behaviour info on a cloud agent")
        self.device.behaviour_info = beh_info
    @dclayMethod(return_="model_mf2c.classes.SharingModelInfo")
    def get_sharing_model_info(self):
        self._check_cloud("Trying to get sharing model info on a cloud agent")
        return self.device.sharing_model_info
    @dclayMethod(return_="model_mf2c.classes.SecurityInfo")
    def get_security_info(self):
        self._check_cloud("Trying to get security info on a cloud agent")
        return self.device.security_info
    @dclayMethod(component="model_mf2c.classes.Component")
    def remove_attached_component(self, component):
        self._check_cloud("Trying to remove an attached component from a cloud agent")
        try:
            self.device.attached_components.remove(component)
        except ValueError:
            pass
    @dclayMethod(sec_info="model_mf2c.classes.SecurityInfo")
    def set_security_info(self, sec_info):
        self._check_cloud("Trying to set security info on a cloud agent")
        self.device.security_info = sec_info
    @dclayMethod(obj='anything', property_name='str', value='anything', beforeUpdate='str', afterUpdate='str')
    def __setUpdate__(self, obj, property_name, value, beforeUpdate, afterUpdate):
        if beforeUpdate is not None:
            getattr(self, beforeUpdate)(property_name, value)
        object.__setattr__(obj, "%s%s" % ("_dataclay_property_", property_name), value)
        if afterUpdate is not None:
            getattr(self, afterUpdate)(property_name, value)
    @dclayMethod(child_id="str", return_= bool)
    def check_child_exists(self, child_id):
        if self.is_leader or self.is_cloud:
            return any((child.id == child_id for child in self.children))
        else:
            raise RuntimeError("Trying to check child on a normal agent")
    @dclayMethod(sharing_info="model_mf2c.classes.SharingModelInfo")
    def set_sharing_model_info(self, sharing_info):
        self._check_cloud("Trying to set sharing model info on a cloud agent")
        self.device.sharing_model_info = sharing_info
    @dclayMethod(bw="int")
    def set_shared_bandwidth_size(self, bw):
        self._check_cloud("Trying to set shared bandwidth size on a cloud agent")
        self.device.sharing_model_info.shared_bandwidth_size = bw
    @dclayMethod(percent="int")
    def set_available_RAM_percent(self, percent):
        self._check_cloud("Trying to set available RAM percent on a cloud agent")
        self.device.dynamic_info.available_RAM_percent = percent
    @dclayMethod(storage="int")
    def set_shared_storage_size(self, storage):
        self._check_cloud("Trying to set shared storage size on a cloud agent")
        self.device.sharing_model_info.shared_storage_size = storage
    @dclayMethod(return_="model_mf2c.classes.BehaviourInfo")
    def get_behaviour_info(self):
        self._check_cloud("Trying to get behaviour info on a cloud agent")
        return self.device.behaviour_info
    @dclayMethod(data="bool")
    def set_data_privacy(self, data):
        self._check_cloud("Trying to set data privacy on a cloud agent")
        self.device.security_info.data_privacy = data
    @dclayMethod(return_="dict")
    def get_resource_info_as_dict(self):
        self._check_cloud("Trying to get resource info on a cloud agent")
        ret = {"Owner": self.device.owner.name}
        ret.update(self.device.static_info.to_dict())
        ret.update(self.device.dynamic_info.to_dict())
        ret.update(self.device.network_info.to_dict())
        ret.update(self.device.behaviour_info.to_dict())
        ret.update(self.device.security_info.to_dict())
        return ret
    @dclayMethod(location="str")
    def set_location(self, location):
        self._check_cloud("Trying to set location on a cloud agent")
        self.device.dynamic_info.location = location
    @dclayMethod(leader="bool")
    def set_leader_capability(self, leader):
        self._check_cloud("Trying to set leader capability on a cloud agent")
        self.device.behaviour_info.leader_capable = leader
    @dclayMethod(percent="int")
    def set_available_storage_percent(self, percent):
        self._check_cloud("Trying to set available storage percent on a cloud agent")
        self.device.dynamic_info.available_storage_percent = percent
    @dclayMethod(mobile="bool")
    def set_mobility(self, mobile):
        self._check_cloud("Trying to set mobility info on a cloud agent")
        self.device.behaviour_info.mobile = mobile
    @dclayMethod(percent="int")
    def set_available_CPU_percent(self, percent):
        self._check_cloud("Trying to set available CPU percent on a cloud agent")
        self.device.dynamic_info.available_CPU_percent = percent
    @dclayMethod(return_="tuple<model_mf2c.classes.User, str, str, model_mf2c.classes.DynamicInfo>")
    def get_dynamic_info(self):
        self._check_cloud("Trying to get dynamic info on a cloud agent")
        return self.device.owner, self.device.static_info.operating_system, self.device.static_info.system_architecture, self.device.dynamic_info
    @dclayMethod(trust="str")
    def set_trust(self, trust):
        self._check_cloud("Trying to set trust info on a cloud agent")
        self.device.behaviour_info.trust = trust
    @dclayMethod(return_="model_mf2c.classes.NetworkInfo")
    def get_network_info(self):
        self._check_cloud("Trying to get network info on a cloud agent")
        return self.device.network_info
    @dclayMethod(return_="tuple<model_mf2c.classes.User, model_mf2c.classes.StaticInfo>")
    def get_static_info(self):
        self._check_cloud("Trying to get static info on a cloud agent")
        return self.device.owner, self.device.static_info
    @dclayMethod(seconds="int")
    def set_remaining_power_seconds(self, seconds):
        self._check_cloud("Trying to set remaining power seconds on a cloud agent")
        self.device.dynamic_info.remaining_power_seconds = seconds
    @dclayMethod(address="str")
    def set_wifi_address(self, address):
        self._check_cloud("Trying to set wifi address on a cloud agent")
        self.device.network_info.wifi_address = address
    @dclayMethod(reliability="str")
    def set_reliability(self, reliability):
        self._check_cloud("Trying to set reliability info on a cloud agent")
        self.device.behaviour_info.reliability = reliability
    @dclayMethod(network="bool")
    def set_network_security(self, network):
        self._check_cloud("Trying to set network security on a cloud agent")
        self.device.security_info.network_security = network
    @dclayMethod(return_="tuple<model_mf2c.classes.User, model_mf2c.classes.StaticInfo, model_mf2c.classes.DynamicInfo, model_mf2c.classes.NetworkInfo, model_mf2c.classes.BehaviourInfo, model_mf2c.classes.SecurityInfo>")
    def get_resource_info(self):
        self._check_cloud("Trying to get resource info on a cloud agent")
        self.device.behaviour_info, self.device.security_info
        return self.device.owner, self.device.static_info, self.device.dynamic_info, self.device.network_info, self.device.behaviour_info, self.device.security_info
    @dclayMethod(info="str")
    def set_wifi_info(self, info):
        self._check_cloud("Trying to set wifi info on a cloud agent")
        self.device.network_info.wifi_info = info
    pass
# End of class definition
# dataClay header
# This is a Stub, to be used for the user client
from dataclay import dclayMethod, DataClayObject

# Imports required by the following class

# Definition of dataClay object class: SharingModelInfo
class SharingModelInfo(DataClayObject):

    @dclayMethod(fields="list<str>", return_="dict")
    def _to_dict(self, fields):
        return {field: self.__getattribute__(field) for field in fields}
    @dclayMethod(obj='anything', property_name='str', value='anything', beforeUpdate='str', afterUpdate='str')
    def __setUpdate__(self, obj, property_name, value, beforeUpdate, afterUpdate):
        if beforeUpdate is not None:
            getattr(self, beforeUpdate)(property_name, value)
        object.__setattr__(obj, "%s%s" % ("_dataclay_property_", property_name), value)
        if afterUpdate is not None:
            getattr(self, afterUpdate)(property_name, value)
    @dclayMethod(RAM_size="int", storage_size="int", CPU_percent="int", bandwidth_size="int")
    def __init__(self, RAM_size, storage_size, CPU_percent, bandwidth_size):
        self.shared_RAM_size = RAM_size
        self.shared_storage_size = storage_size
        self.shared_CPU_percent = CPU_percent
        self.shared_bandwidth_size = bandwidth_size
    @dclayMethod(return_="dict")
    def to_dict(self):
        fields = [
            "shared_RAM_size",
            "shared_storage_size",
            "shared_CPU_percent",
            "shared_bandwidth_size"
        ]
        return self._to_dict(fields)
    pass
# End of class definition
# dataClay header
# This is a Stub, to be used for the user client
from dataclay import dclayMethod, DataClayObject

# Imports required by the following class

# Definition of dataClay object class: SecurityInfo
class SecurityInfo(DataClayObject):

    @dclayMethod(return_="dict")
    def to_dict(self):
        fields = [
            "data_privacy",
            "network_security",
            "device_security"
        ]
        return self._to_dict(fields)
    @dclayMethod(obj='anything', property_name='str', value='anything', beforeUpdate='str', afterUpdate='str')
    def __setUpdate__(self, obj, property_name, value, beforeUpdate, afterUpdate):
        if beforeUpdate is not None:
            getattr(self, beforeUpdate)(property_name, value)
        object.__setattr__(obj, "%s%s" % ("_dataclay_property_", property_name), value)
        if afterUpdate is not None:
            getattr(self, afterUpdate)(property_name, value)
    @dclayMethod(fields="list<str>", return_="dict")
    def _to_dict(self, fields):
        return {field: self.__getattribute__(field) for field in fields}
    @dclayMethod(data_privacy="bool", network_security="bool", device_security="bool")
    def __init__(self, data_privacy, network_security, device_security):
        self.data_privacy = data_privacy
        self.network_security = network_security
        self.device_security = device_security
    pass
# End of class definition
# dataClay header
# This is a Stub, to be used for the user client
from dataclay import dclayMethod, DataClayObject

# Imports required by the following class

# Definition of dataClay object class: User
class User(DataClayObject):

    @dclayMethod(obj='anything', property_name='str', value='anything', beforeUpdate='str', afterUpdate='str')
    def __setUpdate__(self, obj, property_name, value, beforeUpdate, afterUpdate):
        if beforeUpdate is not None:
            getattr(self, beforeUpdate)(property_name, value)
        object.__setattr__(obj, "%s%s" % ("_dataclay_property_", property_name), value)
        if afterUpdate is not None:
            getattr(self, afterUpdate)(property_name, value)
    @dclayMethod(user_id="str", email="str", name="str")
    def __init__(self, user_id, email, name):
        self.id_key = user_id
        self.email = email
        self.name = name
        self.service_consumer = False
        self.resource_contributor = False
        self.allowed_services = []
    @dclayMethod(return_="dict")
    def get_user_profile(self):
        fields = ["id_key", "email", "name", "service_consumer", "resource_contributor"]
        return self._to_dict(fields)
    @dclayMethod(fields="list<str>", return_="dict")
    def _to_dict(self, fields):
        return {field: self.__getattribute__(field) for field in fields}
    pass
# End of class definition
# dataClay header
# This is a Stub, to be used for the user client
from dataclay import dclayMethod, DataClayObject

# Imports required by the following class

# Definition of dataClay object class: DynamicInfo
class DynamicInfo(DataClayObject):

    @dclayMethod(fields="list<str>", return_="dict")
    def _to_dict(self, fields):
        return {field: self.__getattribute__(field) for field in fields}
    @dclayMethod(return_="dict")
    def to_dict(self):
        fields = [
            "available_RAM_size",
            "available_RAM_percent",
            "available_storage_size",
            "available_storage_percent",
            "available_CPU_percent",
            "remaining_power_seconds",
            "remaining_power_percent",
            "location"
        ]
        return self._to_dict(fields)
    @dclayMethod(RAM_size="int", RAM_percent="int", storage_size="int", storage_percent="int", CPU_percent="int", power_seconds="int", power_percent="int", location="str")
    def __init__(self, RAM_size, RAM_percent, storage_size, storage_percent,  CPU_percent, power_seconds, power_percent, location):
        self.available_RAM_size = RAM_size
        self.available_RAM_percent = RAM_percent
        self.available_storage_size = storage_size
        self.available_storage_percent = storage_percent
        self.available_CPU_percent = CPU_percent
        self.remaining_power_seconds = power_seconds
        self.remaining_power_percent = power_percent
        self.location = location
    @dclayMethod(obj='anything', property_name='str', value='anything', beforeUpdate='str', afterUpdate='str')
    def __setUpdate__(self, obj, property_name, value, beforeUpdate, afterUpdate):
        if beforeUpdate is not None:
            getattr(self, beforeUpdate)(property_name, value)
        object.__setattr__(obj, "%s%s" % ("_dataclay_property_", property_name), value)
        if afterUpdate is not None:
            getattr(self, afterUpdate)(property_name, value)
    pass
# End of class definition
# dataClay header
# This is a Stub, to be used for the user client
from dataclay import dclayMethod, DataClayObject

# Imports required by the following class

# Definition of dataClay object class: AggregatedResourceInfo
class AggregatedResourceInfo(DataClayObject):

    @dclayMethod(obj='anything', property_name='str', value='anything', beforeUpdate='str', afterUpdate='str')
    def __setUpdate__(self, obj, property_name, value, beforeUpdate, afterUpdate):
        if beforeUpdate is not None:
            getattr(self, beforeUpdate)(property_name, value)
        object.__setattr__(obj, "%s%s" % ("_dataclay_property_", property_name), value)
        if afterUpdate is not None:
            getattr(self, afterUpdate)(property_name, value)
    @dclayMethod(agent="model_mf2c.classes.Agent")
    def __init__(self, agent):
        self.agent = agent
        self.calculate_aggregation()
    @dclayMethod()
    def calculate_aggregation(self):
        """Update own properties (to be defined).

        This takes info from the agent (device, children, other aggregated info)
        """
        pass
    pass
# End of class definition
