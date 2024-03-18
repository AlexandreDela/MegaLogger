# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'MegaLogger'
copyright = '2024, Alexandre Delaisement'
author = 'Alexandre Delaisement'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import os, sys

src_folder = os.path.abspath("./../../src/megalogger")
sys.path.insert(0, src_folder)
src_folder = os.path.abspath("./../../src/megalogger/abstract_logger.py")
sys.path.insert(0, src_folder)
src_folder = os.path.abspath("./../../src/megalogger/blueprints.py")
sys.path.insert(0, src_folder)
src_folder = os.path.abspath("../../src/megalogger/megalogging.py")
sys.path.insert(0, src_folder)
src_folder = os.path.abspath("./../../src/megalogger/megalogged.py")
sys.path.insert(0, src_folder)
print(src_folder, os.path.exists(src_folder))
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary"
]

autosummary_generate = True

templates_path = ['_templates']
exclude_patterns = []



html_theme = 'furo'
html_static_path = ['_static']
html_theme_options = {
    "light_css_variables":
        {
            "color-brand-primary": "black",
            "color-brand-content": "black"
        },

    "dark_css_variables":
        {
            "color-brand-primary": "white",
            "color-brand-content": "white"
        }
}