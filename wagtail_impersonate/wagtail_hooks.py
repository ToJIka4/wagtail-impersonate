from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.http import HttpRequest

from wagtail import hooks
from wagtail.admin.menu import MenuItem

from wagtail.admin.widgets.button import Button


@hooks.register("register_user_listing_buttons")
def impersonate_user_listing_buttons(user, request_user):
    return [
        Button(
            _("Impersonate"),
            reverse("impersonate-start", args=[user.id]),
        )
    ]


@hooks.register("construct_main_menu")
def register_stop_impersonate_menu_item(request: HttpRequest, items: list):
    if request.user.is_impersonate:
        items.insert(
            0,
            MenuItem(
                _("Stop impersonation"),
                reverse("impersonate-stop"),
                name="Stop impersonation",
                icon_name="snippet",
                order=500,
            ),
        )
