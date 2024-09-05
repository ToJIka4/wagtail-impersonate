  wagtail-impersonate
----

Wagtail extension to allow superusers to "impersonate" other accounts.

**Version:** 0.1.0

**Author:** Stepan Pliaskin (<https://plyask.in/>)

Dependencies
============

-   Wagtail 6.1 and newer.
-   django-impersonate 1.9.4 and newer.

Installation
============

PIP:

    pip install wagtail-impersonate

Use
===

1.  Add `impersonate` and `wagtail-impersonate` to your `INSTALLED_APPS`
2.  Add `impersonate.middleware.ImpersonateMiddleware` to your
    `MIDDLEWARE` setting.
3.  Add `impersonate.urls` somewhere in your url structure. Example:

        urlpatterns = patterns('',
            url(r'^admin/', include(admin.site.urls)),
            url(r'^impersonate/', include('impersonate.urls')),
            ... (all your other urls here) ...
        )

**Note:** The `ImpersonationMiddleware` class should be placed AFTER the
`django.contrib.auth.*` middleware classes

Functionality
=============

To to `Settings` -> `Users`. Find user to impersonate. Press dots (More options for user). Press `Impersonate` button.

To finish impersonation press `Stop impersonation` on admin sidebar.

Settings
========

Since this module is kind of wrap for `django-impersonate` you need to update `settings.py` according to README.md of `django-impersonate`

There are three lines that require attention.

```
IMPERSONATE = {
    "URI_EXCLUSIONS": [],
    "REDIRECT_FIELD_NAME": "next",
    "REDIRECT_URL": "/",
}
```
