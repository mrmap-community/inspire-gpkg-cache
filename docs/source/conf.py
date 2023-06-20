# Configuration file for the Sphinx documentation builder.

# -- Project information
import os
import re
import sys

sys.path.insert(0, os.path.abspath("../.."))

import inspire_gpkg_cache  # noqa


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(os.path.abspath(
        '../..'), package, '__init__.py')).read()
    return re.search("^__version__ = ['\"]([^'\"]+)['\"]",
                     init_py, re.MULTILINE).group(1)


VERSION = get_version("inspire_gpkg_cache")

project = 'inspire-gpkg-cache'
copyright = '2023, MrMap community'
author = 'MrMap community'

release = VERSION
version = VERSION

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'


linkcheck_ignore = [
    r'https://inspire-gpkg-cache.readthedocs.io\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)']
