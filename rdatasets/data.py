# Copyright (c) 2019 Holger Nahrstaedt
# See LICENSE for license details.

from __future__ import division, print_function, absolute_import
import os
import pandas as pd
import pickle

__all__ = ['packages', 'items', 'data', 'get_data_path', 'descr', 'summary']


def packages():
    """Show all package names
    """
    data_dir = os.path.join(os.path.dirname(__file__), '_data')
    ret = []
    for e in os.listdir(data_dir):
        if os.path.isdir(os.path.join(data_dir, e)):
            ret.append(e)
    return ret


def items(package='datasets'):
    """ Returns all dataset items for a given package

        package : string
            package name (default='datasets')

    """
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
    """ Loads data and returns it as DataFrame object

        package : string
            package name (default='datasets')
        item : string
            item name
    """
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


def descr(package, item=None):
    """ Returns a description for a given package/item as markdown text

        package : string
            package name (default='datasets')
        item : string
            item name
    """    
    if item is None:
        item = package
        package = "datasets"

    data_dir = os.path.join(os.path.dirname(__file__), '_data')
    data_package_dir = os.path.join(data_dir, package)
    if not os.path.isdir(data_package_dir):
        print("Which package did you mean: %s?" % str(packages()))
        return None
    data_path = os.path.join(data_dir, 'descr.pickle')
    try:
        with open(data_path, 'rb') as handle:
            descr = pickle.load(handle)
        return descr[package][item]
    except:
        print("Could not read %s/%s" % (package, item))
        print("Which item did you mean: %s?" % str(items(package)))


def get_data_path():
    """Returns the data path of the gzip compressed pickle objects
    """
    return os.path.join(os.path.dirname(__file__), '_data')

def summary():
    """Returns a Dataframe table of all included datasets
    """
    data_dir = os.path.join(os.path.dirname(__file__), '_data')
    data_path = os.path.join(data_dir, 'datasets.pkl.compress')
    try:
        df = pd.read_pickle(data_path, compression ='gzip')
        return df
    except:
        print("Could not read summary")