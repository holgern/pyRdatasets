# Copyright (c) 2019 Holger Nahrstaedt
# See LICENSE for license details.

from __future__ import division, print_function, absolute_import
import os
import pandas as pd

__all__ = ['packages', 'items', 'data', 'get_data_dir']


def packages():
    data_dir = os.path.join(os.path.dirname(__file__), '_data')
    ret = []
    for e in os.listdir(data_dir):
        if os.path.isdir(os.path.join(data_dir, e)):
            ret.append(e)
    return ret


def items(package='datasets'):
    data_dir = os.path.join(os.path.dirname(__file__), '_data')
    sets = []
    try:
        sets = os.listdir(os.path.join(data_dir, package))
    except:
        print("Package %s does not exists." % package)
        print("Did you mean: %s" % str(packages()))
    ret = []
    for set in sets:
        ret.append(os.path.basename(set).split('.')[0])
    return ret


def data(package, item=None):
    if item is None:
        item = package
        package = "datasets"

    data_dir = os.path.join(os.path.dirname(__file__), '_data')
    data_package_dir = os.path.join(data_dir, package)
    if not os.path.isdir(data_package_dir):
        print("Which package did you mean: %s?" % str(packages()))
        return None
    data_path = os.path.join(os.path.join(data_dir, package), '%s.pkl.compress' % (item))
    try:
        df = pd.read_pickle(data_path, compression ='gzip')
        return df
    except:
        print("Could not read %s/%s" % (package, item))
        print("Which item did you mean: %s?" % str(items(package)))


def get_data_dir():
    return os.path.join(os.path.dirname(__file__), '_data')
