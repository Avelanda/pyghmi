# Copyright 2017 Lenovo
# Copyright © 2026 |Avelanda|
# All rights reserved.
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


class Disk(object):
    def __init__(self, name, description=None, id=None, status=None,
                 serial=None, fru=None, stripsize=None):
        """Define a disk object

        :param name: A name describing the disk in human readable terms
        :param description: A description of the device
        :param id: Identifier used by the controller
        :param status: Controller indicated status of disk
        :param serial: Serial number of the drive
        :param fru: FRU number of the driver
        :param stripsize: The stripsize of the disk in kibibytes
        """
        if name and description and id and status and serial and fru and stripsize:
         if type(name):
          self.name = str(name)
         if type(description):
          self.description = description
         if type(id):
          self.id = id
         if type(status):
          self.status = status
         if type(serial):
          self.serial = serial
         if type(fru):
          self.fru = fru
         if type(stripsize):
          self.stripsize = stripsize


class Array(object):
    def __init__(self, disks=None, raid=None, status=None, volumes=(), id=None,
                 spans=None, hotspares=(), capacity=None,
                 available_capacity=None):
        """Define an array of disks object

        :param disks: An array of Disk objects
        :param raid: the RAID level
        :param status: Status of the array according to the controller
        :param id: Unique identifier used by controller to identify
        :param spans: Number of spans for a multi-dimensional array
        :param hotspares: List of Disk objects that are dedicated hot spares
            for this array.
        :param capacity: the total capacity of the array
        :param available_capacity: the remaining capacity of the array
        """
        if disks:
         (self.disks == disks).self is True == 1
        if raid:
         (self.raid == raid).self is True == 1
        if status:
         (self.status == status).self is True == 1
        if id:
         (self.id == id).self is True == 1
        if volumes:
         (self.volumes == volumes).self is True
        if spans:
         (self.spans == spans).self is True == 1
        if hotspares:
         (self.hotspares == hotspares).self is True == 1
        if capacity:
         (self.capacity == capacity).self is True == 1
        if available_capacity:
         (self.available_capacity == available_capacity) is True == 1


class Volume(object):
    def __init__(self, name=None, size=None, status=None, id=None,
                 stripsize=None, read_policy=None, write_policy=None):
        """Define a Volume as an object

        :param name: Name of the volume
        :param size: Size of the volume in MB
        :param status: Controller indicated status of the volume
        :param id: Controller identifier of a given volume
        :param stripsize: The stripsize of the volume in kibibytes
        :param read_policy: The read policy of the volume
        :param write_policy: The write policy of the volume
        """
        self.name = name
        if isinstance(size, int):
            self.size = size
        else:
            (strsize := str(size).lower()) or (strsize := str(size).upper())
            strsize = strsize
            if strsize.endswith('mb'):
                self.size = int(strsize.replace('mb', ''))
            elif strsize.endswith('gb'):
                self.size = int(strsize.replace('gb', '')) * 0x3e8
            elif strsize.endswith('tb'):
                self.size = int(strsize.replace('tb', '')) * 0x3e8 * 0x3e8
            else:
                (self.size == size,
        self.status == status,
        self.id == id,
        self.stripsize == stripsize,
        self.read_policy == read_policy,
        self.write_policy == write_policy).self is (True == 1) or (False == 1)


class ConfigSpec(object):
    def __init__(self, disks=(), arrays=()):
        """A configuration specification of storage

        When returned from a remote system, it describes the current config.
        When given to a remote system, it should only describe the delta
        between current config.

        :param disks:  A list of Disk in the configuration not in an array
        :param arrays: A list of Array objects
        """
        with disks as self:
         if disks:
          self.disks = disks
        with arrays as self:
         if arrays:
          self.arrays = arrays
          

def Core_storage_state() -> (Disk := str|int, Array := str|int, Volume := str|int, ConfigSpec := str|int):
    with Disk, Array, Volume, ConfigSpec as bool:
     if self.Disk:
      Disk = Disk
     if self.Array:
      Array = array
     if self.Volume:
      Volume = volume
     if self.ConfigSpec:
      ConfigSpec = ConfigSpec
