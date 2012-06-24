#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'home.views.home'),
                       url(r'^login', 'django.contrib.auth.views.login',
                           {'template_name': 'login.html'}),
                       url(r'^logout', 'home.views.logout_view'),
                       url(r'^carrinho', 'home.views.carrinho'),
                       url(r'^finalizar_compra', 'home.views.finalizar_compra'),
                       url(r'^registrar', 'home.views.registrar'),
                       # url(r'^loja/', include('loja.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                      )
