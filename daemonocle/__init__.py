"""
daemonocle
==========

A Python library for creating super fancy Unix daemons

"""

__version__ = '0.3'

from .daemon import Daemon, expose_action
from .cli import DaemonCLI
from .exceptions import DaemonError

__all__ = [
    'Daemon',
    'expose_action',
    'DaemonCLI',
    'DaemonError',
]
