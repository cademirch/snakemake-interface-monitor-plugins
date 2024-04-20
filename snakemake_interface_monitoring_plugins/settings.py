__author__ = "Christopher Tomkins-Tinch, Johannes Köster"
__copyright__ = "Copyright 2023, Christopher Tomkins-Tinch, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

from dataclasses import dataclass, field
from typing import Optional

import snakemake_interface_common.plugin_registry.plugin


@dataclass
class MonitoringProviderSettingsBase(
    snakemake_interface_common.plugin_registry.plugin.SettingsBase
):
    """Base class for Monitoring plugin settings.

    Storage plugins can define a subclass of this class,
    named 'MonitoringSettings'.
    """
    metadata: Optional[dict] = field(
        default=None,
        metadata={
            "help": "Metadata to pass to monitoring provider",
            "env_var": False,
        },
    )
    token: Optional[str] = field(
        default=None,
        metadata={
            "help": "Auth token for monitoring plugin.",
            "env_var": True,
        },
    )
