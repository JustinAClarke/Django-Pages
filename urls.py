"""
    Django Pages (Very Very Basic CMS) Justin Fuhrmeister-Clarke.
    Copyright (C) 2017  Justin Fuhrmeiser-Clarke <justin@fuhrmeister-clarke.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    """
    
from django.conf.urls import url
from django.views.generic.base import RedirectView


from pages import views

app_name = 'pages'

urlpatterns = [
    #favicon
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/pages/image/favicon.svg', permanent=True)),

    # ex: /pages/
    url(r'^$', views.index, name='index'),

    #admin list photos/tags
    # ex: /pages/admin_list/
    url(r'^admin_list/$', views.admin_list, name='admin_list'),
        
    # ex: /pages/page/edit/
    url(r'^page/edit/(?P<id>[0-9]+)/$', views.edit_page, name='edit_page'),
    
    # ex: /pages/page/delete/
    url(r'^page/delete/(?P<id>[0-9]+)/$', views.delete_page, name='delete_page'),
    
    # ex: /pages/page/add/
    url(r'^page/add/$', views.add_page, name='add_page'),
    
    # ex: /pages/page/
    url(r'^page/(?P<url_var>\w+)/$', views.page, name='page'),
    
    # ex: /pages/nav/edit/
    url(r'^nav/edit/(?P<id>[0-9]+)/$', views.edit_nav, name='edit_nav'),
    
    # ex: /pages/nav/add/
    url(r'^nav/add/$', views.add_nav, name='add_nav'),
    
    # ex: /pages/nav/delete/
    url(r'^nav/delete/(?P<id>[0-9]+)/$', views.delete_nav, name='delete_nav'),

    # ex: /pages/contact/
    url(r'^contact/$', views.contact, name='contact'),
    
    # ex: /pages/contact/list
    url(r'^contact/list$', views.contact_list, name='contact_list'),
    
    # ex: /pages/contact/view
    url(r'^contact/view/(?P<id>[0-9]+)/$', views.contact_view, name='contact_view'),
    
    # ex: /pages/contact/view
    url(r'^contact/delete/(?P<id>[0-9]+)/$', views.contact_delete, name='contact_delete'),

    url(r'^test/(?P<page>[0-9]+)/$', views.test, name='test'),
    
]

