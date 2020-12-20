"""Compile static assets."""
from flask import current_app as app
from flask_assets import Bundle

def compile_static_assets(assets):
    """Create stylesheet bundles."""
    assets.auto_build = True
    assets.debug = False
    common_less_bundle = Bundle(
        "src/less/*.less",
        filters="less,cssmin",
        output="dist/css/style.css",
        extra={"rel": "stylesheet/less"},
    )
    home_less_bundle = Bundle(
        "home_bp/src/less/*.less",
        filters="less,cssmin",
        output="dist/css/home.css",
        extra={"rel": "stylesheet/less"},
    )
    auth_less_bundle = Bundle(
        "auth_bp/src/less/*.less",
        filters="less,cssmin",
        output="dist/css/auth.css",
        extra={"rel": "stylesheet/less"},
    )
    assets.register("common_less_bundle", common_less_bundle)
    assets.register("home_less_bundle", home_less_bundle)
    assets.register("auth_less_bundle", auth_less_bundle)
    if app.config["FLASK_ENV"] == "development":
        common_less_bundle.build()
        home_less_bundle.build()
        auth_less_bundle.build()
    return assets
