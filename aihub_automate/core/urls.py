# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    #path('accounts/', include('django.contrib.auth.urls')),
    path("", include("apps.authentication.urls")), # Auth routes - login / register

    # ADD NEW Routes HERE
    path("", include("apps.AIHUB.urls")),
    # Leave `Home.Urls` as last the last line
    #path("", include("apps.home.urls"))
    path("fin/", include("apps.DC_Finance.urls")),
]
