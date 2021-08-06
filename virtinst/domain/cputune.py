# Copyright (c) 2018 Oracle and/or its affiliates. All rights reserved.
#
# This work is licensed under the GNU GPLv2 or later.
# See the COPYING file in the top-level directory.

from ..xmlbuilder import XMLBuilder, XMLProperty, XMLChildProperty


###############
# CPU Pinning #
###############

class _VCPUPin(XMLBuilder):
    """
    Class for generating <cputune> child <vcpupin> XML
    """
    XML_NAME = "vcpupin"
    _XML_PROP_ORDER = ["vcpu", "cpuset"]

    vcpu = XMLProperty("./@vcpu", is_int=True)
    cpuset = XMLProperty("./@cpuset")


class _IOThreadPin(XMLBuilder):
    """
    Class for generating <cputune> child <iothreadpin> XML
    """
    XML_NAME = "iothreadpin"
    _XML_PROP_ORDER = ["iothread", "cpuset"]

    iothread = XMLProperty("./@iothread", is_int=True)
    cpuset = XMLProperty("./@cpuset")


class _CacheCPU(XMLBuilder):
    """
    Class for generating <cachetune> child <cache> XML
    """
    XML_NAME = "cache"
    _XML_PROP_ORDER = ["level", "id", "type", "size", "unit"]

    level = XMLProperty("./@level", is_int=True)
    id = XMLProperty("./@id", is_int=True)
    type = XMLProperty("./@type")
    size = XMLProperty("./@size", is_int=True)
    unit = XMLProperty("./@unit")


class _CacheTuneCPU(XMLBuilder):
    """
    Class for generating <cputune> child <cachetune> XML
    """
    XML_NAME = "cachetune"
    _XML_PROP_ORDER = ["vcpus", "caches"]

    vcpus = XMLProperty("./@vcpus")
    caches = XMLChildProperty(_CacheCPU)


class _NodeCPU(XMLBuilder):
    """
    Class for generating <memorytune> child <node> XML
    """
    XML_NAME = "node"
    _XML_PROP_ORDER = ["id", "bandwidth"]

    id = XMLProperty("./@id", is_int=True)
    bandwidth = XMLProperty("./@bandwidth", is_int=True)


class _MemoryTuneCPU(XMLBuilder):
    """
    Class for generating <cputune> child <memorytune> XML
    """
    XML_NAME = "memorytune"

    vcpus = XMLProperty("./@vcpus")
    nodes = XMLChildProperty(_NodeCPU)


class _VCPUSched(XMLBuilder):
    """
    Class for generating <cputune> child <vcpusched> XML
    """
    XML_NAME = "vcpusched"
    _XML_PROP_ORDER = ["vcpus", "scheduler", "priority"]

    vcpus = XMLProperty("./@vcpus")
    scheduler = XMLProperty("./@scheduler")
    priority = XMLProperty("./@priority", is_int=True)


class DomainCputune(XMLBuilder):
    """
    Class for generating <cpu> XML
    """
    XML_NAME = "cputune"
    _XML_PROP_ORDER = ["shares", "period", "quota", "global_period", "global_quota",
            "emulator_period", "emulator_quota", "iothread_period", "iothread_quota",
            "vcpupins", "emulatorpin_cpuset", "iothreadpins",
            "cachetunes", "memorytunes", "vcpuscheds"]

    # Resource quotas
    shares = XMLProperty("./shares", is_int=True)
    period = XMLProperty("./period", is_int=True)
    quota = XMLProperty("./quota", is_int=True)
    global_period = XMLProperty("./global_period", is_int=True)
    global_quota = XMLProperty("./global_quota", is_int=True)
    emulator_period = XMLProperty("./emulator_period", is_int=True)
    emulator_quota = XMLProperty("./emulator_quota", is_int=True)
    iothread_period = XMLProperty("./iothread_period", is_int=True)
    iothread_quota = XMLProperty("./iothread_quota", is_int=True)

    # CPU Pinning
    vcpupins = XMLChildProperty(_VCPUPin)
    emulatorpin_cpuset = XMLProperty("./emulatorpin/@cpuset")
    iothreadpins = XMLChildProperty(_IOThreadPin)
    cachetunes = XMLChildProperty(_CacheTuneCPU)
    memorytunes = XMLChildProperty(_MemoryTuneCPU)
    vcpuscheds = XMLChildProperty(_VCPUSched)
