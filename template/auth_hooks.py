"""Hook into Alliance Auth"""

# Django
# Alliance Auth
from django.utils.translation import gettext_lazy as _

from allianceauth import hooks
from allianceauth.services.hooks import MenuItemHook, UrlHook

from . import app_settings, urls


class TemplateMenuItem(MenuItemHook):
    """This class ensures only authorized users will see the menu entry"""

    def __init__(self):
        super().__init__(
            f"{app_settings.TEMPLATE_APP_NAME}",
            "fas fa-book fa-fw",
            "template:index",
            navactive=["template:"],
        )

    def render(self, request):
        if request.user.has_perm("template.basic_access"):
            return MenuItemHook.render(self, request)
        return ""


@hooks.register("menu_item_hook")
def register_menu():
    """Register the menu item"""

    return TemplateMenuItem()


@hooks.register("url_hook")
def register_urls():
    """Register app urls"""

    return UrlHook(urls, "template", r"^template/")
