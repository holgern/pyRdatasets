# Copyright (c) 2019 Holger Nahrstaedt
# See LICENSE for license details.

from __future__ import division, print_function, absolute_import
import os
import pandas as pd

__all__ = ['groups', 'sets', 'load', 'get_data_dir']


def groups():
    data_dir = os.path.join(os.path.dirname(__file__), '_data')
    ret = []
    for e in os.listdir(data_dir):
        if os.path.isdir(os.path.join(data_dir, e)):
            ret.append(e)
    return ret


def sets(group='datasets'):
    data_dir = os.path.join(os.path.dirname(__file__), '_data')
    try:
        sets = os.listdir(os.path.join(data_dir, group))
    except:
        print("%s does not exists" % group)
    ret = []
    for set in sets:
        ret.append(os.path.basename(set).split('.')[0])
    return ret


def load(group, set=None):
    if set is None:
        set = group
        group = "datasets"

    data_dir = os.path.join(os.path.dirname(__file__), '_data')
    data_path = os.path.join(os.path.join(data_dir, group), '%s.pkl.compress' % (set))
    try:
        df = pd.read_pickle(data_path, compression ='gzip')
        return df
    except:
        print("Could not read %s/%s" % (group, set))


def get_data_dir():
    return os.path.join(os.path.dirname(__file__), '_data')
