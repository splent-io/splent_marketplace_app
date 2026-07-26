"""
Configuration for splent_marketplace_app.

Each class extends the framework's base configuration. Only override
what your product needs — everything else is inherited automatically.

Hierarchy (later layers win):
  1. Framework defaults (Config base class)
  2. This file (product config)
  3. Feature inject_config() calls
"""

from splent_framework.configuration.default_config import (
    DevelopmentConfig as BaseDev,
    TestingConfig as BaseTest,
    ProductionConfig as BaseProd,
)


class _SiteConfig:
    """Site-level configuration — consumed by the theme (header, footer, SEO).

    The main navigation is NOT declared here: each installed feature registers
    its entry via register_nav_item() (marketplace, product lines,
    configurator), so the menu tracks the product's derivation.
    """

    SITE_NAME = "SPLENT Marketplace"
    SITE_TAGLINE = (
        "Reusable features and product lines for SPLENT products. "
        "Search, inspect and install with one command."
    )
    SITE_SOCIAL = [
        {"network": "GitHub", "href": "https://github.com/splent-io"},
        {"network": "splent.io", "href": "https://splent.io"},
        {"network": "Docs", "href": "https://docs.splent.io"},
    ]


class DevelopmentConfig(_SiteConfig, BaseDev):
    # Add product-specific dev settings here.
    # Example: EXPLAIN_TEMPLATE_LOADING = True
    pass


class TestingConfig(_SiteConfig, BaseTest):
    # Add product-specific test settings here.
    # Example: PRESERVE_CONTEXT_ON_EXCEPTION = False
    pass


class ProductionConfig(_SiteConfig, BaseProd):
    # Add product-specific production settings here.
    # Example: SESSION_COOKIE_SECURE = True
    pass
