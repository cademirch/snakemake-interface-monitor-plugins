__author__ = "Cade Mirchandani, Christopher Tomkins-Tinch, Johannes Köster"
__copyright__ = (
    "Copyright 2023, Cade Mirchandani, Christopher Tomkins-Tinch, Johannes Köster"
)
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

import types
from typing import List, Mapping

from snakemake_interface_monitor_plugins.settings import (
    MonitorProviderSettingsBase,
)
from snakemake_interface_common.plugin_registry.attribute_types import (
    AttributeKind,
    AttributeMode,
    AttributeType,
)
from snakemake_interface_monitor_plugins.registry.plugin import Plugin
from snakemake_interface_common.plugin_registry import PluginRegistryBase
from snakemake_interface_monitor_plugins import common
from snakemake_interface_monitor_plugins.monitor_provider import (
    MonitorProviderBase,
)


class MonitorPluginRegistry(PluginRegistryBase):
    """This class is a singleton that holds all registered executor plugins."""

    @property
    def module_prefix(self) -> str:
        return common.monitor_plugin_module_prefix

    def load_plugin(self, name: str, module: types.ModuleType) -> Plugin:
        """Load a plugin by name."""

        return Plugin(
            _name=name,
            monitor_provider=module.MonitorProvider,
            _monitor_settings_cls=getattr(module, "MonitorProviderSettings", None),
        )

    def expected_attributes(self) -> Mapping[str, AttributeType]:
        return {
            "MonitorSettings": AttributeType(
                cls=MonitorProviderSettingsBase,
                mode=AttributeMode.OPTIONAL,
                kind=AttributeKind.CLASS,
            ),
            "MonitorProvider": AttributeType(
                cls=MonitorProviderBase,
                mode=AttributeMode.REQUIRED,
                kind=AttributeKind.CLASS,
            ),
        }
