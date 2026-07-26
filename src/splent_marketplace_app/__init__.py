from splent_framework.app_factory import create_splent_app
from splent_framework.nav.nav_registry import register_nav_item


def create_app(config_name="development"):
    app = create_splent_app(__name__, config_name)
    # Cross-links to the other SPLENT web properties (product-level nav).
    register_nav_item("splent_docs", "Docs", "https://docs.splent.io", order=900, icon="book-open")
    register_nav_item("splent_site", "splent.io", "https://splent.io", order=910, icon="globe")
    return app
