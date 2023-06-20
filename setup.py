import os
import re

from setuptools import find_namespace_packages, setup

name = 'inspire-gpkg-cache'
package = 'inspire_gpkg_cache'
description = 'A simple lib to cache spatial data which is published conform to the rules of the European SDI (INSPIRE)'
url = 'https://github.com/mrmap-community/inspire-gpkg-cache'
author = 'mrmap-community'
author_email = 'armin.retterath@vermkv.rlp.de'
license = 'MIT'


with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("^__version__ = ['\"]([^'\"]+)['\"]",
                     init_py, re.MULTILINE).group(1)


version = get_version(package)

setup(
    name=name,
    version=version,
    url=url,
    license=license,
    description=description,
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author=author,
    author_email=author_email,
    packages=[p for p in find_namespace_packages(
        exclude=('tests*',)) if p.startswith(package)],
    include_package_data=True,
    install_requires=[
        "shapely>=2.0.1",
        # FIXME: find a way to install the correct version for gdal pypi package on build stages.
        # "gdal>=3.0.4", do not add this here. The version which will be installed for build depends on system gdal version.
        # "gdal_utils>=3.7.0.0",
        "owslib>=0.25.0",
        "requests>=2.31.0",
        "python-slugify>=8.0.1",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
