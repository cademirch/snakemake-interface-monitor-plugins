__author__ = "Christopher Tomkins-Tinch, Johannes Köster"
__copyright__ = "Copyright 2023, Christopher Tomkins-Tinch, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

from dataclasses import dataclass
from typing import Optional, Type
from snakemake_interface_monitoring_plugins.settings import (
    MonitoringProviderSettingsBase,
)
from snakemake_interface_monitoring_plugins import common

from snakemake_interface_common.plugin_registry.plugin import PluginBase


@dataclass
class Plugin(PluginBase):
    monitoring_proivder: object
    _monitoring_settings_cls: Optional[Type[MonitoringProviderSettingsBase]]
    _name: str

    @property
    def name(self):
        return self._name

    @property
    def cli_prefix(self):
        return "monitoring-" + self.name.replace(
            common.monitoring_plugin_module_prefix, ""
        )

    @property
    def settings_cls(self):
        return self._monitoring_settings_cls
