# Configuration file for the Sphinx documentation builder.

# -- Project information

project = "wrims-docs"
copyright = "2026, CA Department of Water Resources"
author = "Zachary Roy"

release = "0.1"
version = "0.1.0"

# -- General configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "myst_parser",
]

intersphinx_mapping = {
    "wrims-engine": (
        "https://wrims-docs.readthedocs.io/projects/wrims-engine/en/latest",
        None,
    ),
    "wrims-gui": (
        "https://wrims-docs.readthedocs.io/projects/wrims-gui/en/latest",
        None,
    ),
    "wresl": (
        "https://wrims-docs.readthedocs.io/projects/wresl/en/latest",
        None,
    ),
}
intersphinx_disabled_reftypes = ["std:doc", "std:label"]

templates_path = ["_templates"]

# -- Options for HTML output

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "home_page_in_toc": True,
    "max_navbar_depth": 3,
}

# -- Options for EPUB output
epub_show_urls = "footnote"
