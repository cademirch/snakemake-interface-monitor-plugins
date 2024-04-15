__author__ = "Christopher Tomkins-Tinch, Johannes Köster"
__copyright__ = "Copyright 2023, Christopher Tomkins-Tinch, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

import types
from typing import List, Mapping

from snakemake_interface_monitoring_plugins.settings import (
    MonitoringProviderSettingsBase,
)
from snakemake_interface_common.plugin_registry.attribute_types import (
    AttributeKind,
    AttributeMode,
    AttributeType,
)
from snakemake_interface_monitoring_plugins.registry.plugin import Plugin
from snakemake_interface_common.plugin_registry import PluginRegistryBase
from snakemake_interface_monitoring_plugins import common
from snakemake_interface_monitoring_plugins.monitoring_provider import (
    MonitoringProviderBase,
)


class MonitoringPluginRegistry(PluginRegistryBase):
    """This class is a singleton that holds all registered executor plugins."""

    def get_registered_read_write_plugins(self) -> List[str]:
        return [
            plugin.name
            for plugin in self.plugins.values()
            if plugin.monitoring_provider.is_read_write
        ]

    @property
    def module_prefix(self) -> str:
        return common.monitoring_plugin_module_prefix

    def load_plugin(self, name: str, module: types.ModuleType) -> Plugin:
        """Load a plugin by name."""
        return Plugin(
            _name=name,
            monitoring_provider=module.MonitoringProvider,
            monitoring_object=module.MonitoringObject,
            _monitoring_settings_cls=getattr(
                module, "MonitoringProviderSettings", None
            ),
        )

    def expected_attributes(self) -> Mapping[str, AttributeType]:
        return {
            "monitoringSettings": AttributeType(
                cls=MonitoringProviderSettingsBase,
                mode=AttributeMode.OPTIONAL,
                kind=AttributeKind.CLASS,
            ),
            "monitoringProvider": AttributeType(
                cls=MonitoringProviderBase,
                mode=AttributeMode.REQUIRED,
                kind=AttributeKind.CLASS,
            ),
        }
