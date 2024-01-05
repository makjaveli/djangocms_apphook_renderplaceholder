from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.urls import include, path
from shop_app import views


@apphook_pool.register  # register the application
class ShopAppHook(CMSApp):
    app_name = "shop_app"
    name = "Shop Application"
#    permissions = True

    def get_urls(self, page=None, language=None, **kwargs):

        return [
            path('<str:slug>/', views.product_view)
        ]
