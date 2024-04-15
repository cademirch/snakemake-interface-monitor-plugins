__author__ = "Christopher Tomkins-Tinch, Johannes Köster"
__copyright__ = "Copyright 2023, Christopher Tomkins-Tinch, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

from abc import ABC, abstractmethod
from typing import Optional
from snakemake_interface_monitoring_plugins.settings import (
    MonitoringProviderSettingsBase,
)


class MonitorBase(ABC):
    def __init__(
        self, settings: Optional[MonitoringProviderSettingsBase] = None
    ) -> None:
        self.settings = settings
        self.__post_init__()

    def __post_init__(self):  # noqa B027
        pass

    @abstractmethod
    def log_handler(self, msg: dict) -> None:
        pass
