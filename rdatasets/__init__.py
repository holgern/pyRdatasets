# Copyright (c) 2019-2024 Holger Nahrstaedt
# See LICENSE for license details.


from .rdatasets import data, descr, get_data_path, items, packages, summary


__all__ = [
    'packages',
    'items',
    'data',
    'get_data_path',
    'descr',
    'summary',
    '__version__',
]

try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"
