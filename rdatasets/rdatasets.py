# Copyright (c) 2019-2024 Holger Nahrstaedt
# See LICENSE for license details.


import os
import pickle

import pandas as pd


def packages():
    """Show all package names."""
    data_dir = os.path.join(os.path.dirname(__file__), '_data')
    ret = []
    for e in os.listdir(data_dir):
        if os.path.isdir(os.path.join(data_dir, e)):
            ret.append(e)
    return ret


def items(package='datasets'):
    """Returns all dataset items for a given package.

    package : string
        package name (default='datasets')
    """
    data_dir = os.path.join(os.path.dirname(__file__), '_data')
    package_dir = os.path.join(data_dir, package)
    if not os.path.exists(package_dir):
        print("Package %s does not exist." % package)
        print("Did you mean: %s" % str(packages()))
        return []
    return [os.path.splitext(e)[0] for e in os.listdir(package_dir)]


def data(package, item=None):
    """Loads data and returns it as DataFrame object.

    package : string
        package name (default='datasets')
    item : string
        item name
    """
    if item is None:
        item = package
        package = "datasets"

    data_dir = os.path.join(os.path.dirname(__file__), '_data')
    package_dir = os.path.join(data_dir, package)
    data_path = os.path.join(package_dir, f'{item}.pkl.compress')

    if not os.path.exists(package_dir):
        print(f"Package {package} does not exist.")
        print("Available packages: %s" % str(packages()))
        return None

    if not os.path.exists(data_path):
        print(f"Item {item} does not exist in package {package}.")
        print("Available items: %s" % str(items(package)))
        return None

    try:
        df = pd.read_pickle(data_path, compression='xz')
        return df
    except Exception as e:
        print(f"Could not read {package}/{item} due to {e}")
        return None


def descr(package, item=None):
    """Returns a description for a given package/item as markdown text.

    package : string
        package name (default='datasets')
    item : string
        item name
    """
    if item is None:
        item = package
        package = "datasets"

    data_dir = os.path.join(os.path.dirname(__file__), '_data')
    data_path = os.path.join(data_dir, 'descr.pickle')

    try:
        with open(data_path, 'rb') as handle:
            descr = pickle.load(handle)
        return descr.get(package, {}).get(item)
    except Exception as e:
        print(f"Could not read {package}/{item} due to {e}")
        return None


def get_data_path():
    """Returns the data path of the xz compressed pickle objects."""
    return os.path.join(os.path.dirname(__file__), '_data')


def summary():
    """Returns a Dataframe table of all included datasets."""
    data_dir = os.path.join(os.path.dirname(__file__), '_data')
    data_path = os.path.join(data_dir, 'datasets.pkl.compress')

    try:
        df = pd.read_pickle(data_path, compression='xz')
        return df
    except Exception as e:
        print(f"Could not read summary: {e}")
        return None
