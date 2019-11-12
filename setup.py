#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import sys
import subprocess
import setuptools
from functools import partial

from setuptools import setup, Extension
from distutils.sysconfig import get_python_inc


MAJOR = 0
MINOR = 1
MICRO = 0
ISRELEASED = True
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)

# Return the git revision as a string
def git_version():
    def _minimal_ext_cmd(cmd):
        # construct minimal environment
        env = {}
        for k in ['SYSTEMROOT', 'PATH']:
            v = os.environ.get(k)
            if v is not None:
                env[k] = v
        # LANGUAGE is used on win32
        env['LANGUAGE'] = 'C'
        env['LANG'] = 'C'
        env['LC_ALL'] = 'C'
        out = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                               env=env).communicate()[0]
        return out

    try:
        out = _minimal_ext_cmd(['git', 'rev-parse', 'HEAD'])
        GIT_REVISION = out.strip().decode('ascii')
    except OSError:
        GIT_REVISION = "Unknown"

    return GIT_REVISION


def get_version_info():
    # Adding the git rev number needs to be done inside
    # write_version_py(), otherwise the import of Rdatasets.version messes
    # up the build under Python 3.
    FULLVERSION = VERSION
    if os.path.exists('.git'):
        GIT_REVISION = git_version()
    elif os.path.exists('rdatasets/version.py'):
        # must be a source distribution, use existing version file
        # load it as a separate module to not load pywt/__init__.py
        import imp
        version = imp.load_source('rdatasets.version', 'rdatasets/version.py')
        GIT_REVISION = version.git_revision
    else:
        GIT_REVISION = "Unknown"

    if not ISRELEASED:
        FULLVERSION += '.dev0+' + GIT_REVISION[:7]

    return FULLVERSION, GIT_REVISION


def write_version_py(filename='rdatasets/version.py'):
    cnt = """
# THIS FILE IS GENERATED FROM rdatasets SETUP.PY
short_version = '%(version)s'
version = '%(version)s'
full_version = '%(full_version)s'
git_revision = '%(git_revision)s'
release = %(isrelease)s

if not release:
    version = full_version
"""
    FULLVERSION, GIT_REVISION = get_version_info()

    with open(filename, 'w') as a:
        a.write(cnt % {'version': VERSION,
                       'full_version': FULLVERSION,
                       'git_revision': GIT_REVISION,
                       'isrelease': str(ISRELEASED)})


if __name__ == '__main__':

    # Rewrite the version file everytime
    write_version_py()
    
    setup(
        name="rdatasets",
        maintainer="Holger Nahrstaedt",
        maintainer_email="holger@nahrstaedt.de",
        url="https://github.com/holgern/pyRdatasets",
        license="GPLv3",
        description="package that provides over 1000 datasets from various R packages",
        long_description=open('README.md').read(),
        long_description_content_type='text/markdown',
        keywords=["rdatasets", "datasets"],
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "Intended Audience :: Education",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Operating System :: OS Independent",
            "Programming Language :: C",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Topic :: Software Development :: Libraries :: Python Modules"
        ],
        platforms=["Windows", "Linux", "Solaris", "Mac OS-X", "Unix"],
        version=get_version_info()[0],
        packages=['rdatasets','rdatasets._data'],
        package_data={'rdatasets._data': ['*/*.pkl.compress', '*.pkl.compress', '*.pickle']},
        install_requires=["pandas"],
    )

