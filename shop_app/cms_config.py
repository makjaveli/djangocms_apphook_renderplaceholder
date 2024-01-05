from cms.app_base import CMSAppConfig

from shop_app import models, views


class ShopAppConfig(CMSAppConfig):
    cms_enabled = True
    cms_toolbar_enabled_models = [(models.Product, views.render_product)]
