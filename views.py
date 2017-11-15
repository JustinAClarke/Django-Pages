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
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponseForbidden

# Create your views here.

from .models import Page
from .forms import *

def getTitle(title=False):
    if(title):
        return getTitle() + " - " + title
    else:
        return "Justin Fuhrmeister-Clarke"


def index(request):
    context = {'title':getTitle(),'request': request}
    return render(request, 'pages/index.html', context)

def admin_list(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('photos:index'))
    pages = Page.objects.all().order_by('title')
    navs = Nav.objects.all().order_by('title')

    context = {'title':getTitle(), 'request': request,'pages':pages,'navs':navs}
    return render(request, 'pages/admin_list.html', context)




def add_page(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('pages:index'))
    if request.method == "POST":
        page = PageForm(request.POST) # A form bound to the POST data
        if page.is_valid(): # All validation rules pass
            new_page = page.save()
            return HttpResponseRedirect(reverse('pages:admin_list'))
    else:
        page = PageForm()
    context = {'title':getTitle(), 'request': request,'form':page}
    return render(request, 'pages/add.html', context)
    
def edit_page(request,id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('pages:index'))
    page = get_object_or_404(Page, pk=id)
    if request.method == "POST":
        page = PageForm(request.POST,instance=page) # A form bound to the POST data
        if page.is_valid(): # All validation rules pass
            new_page = page.save()
            return HttpResponseRedirect(reverse('pages:admin_list'))
    else:
        data={'title':page.title,
            'url':page.url,
            'content':page.content,
        }
        page = PageForm(data)
    context = {'title':getTitle(), 'request': request,'form':page}
    return render(request, 'pages/add.html', context)

def page(request,url_var):
    
    page_var = get_object_or_404(Page, url=url_var)

    context = {'title':getTitle(page_var.title),'request': request,'data':page_var}
    return render(request, 'pages/page.html', context)


def add_nav(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('pages:index'))
    if request.method == "POST":
        nav = NavForm(request.POST) # A form bound to the POST data
        if nav.is_valid(): # All validation rules pass
            new_nav = nav.save()
            return HttpResponseRedirect(reverse('pages:admin_list'))
    else:
        nav = NavForm()
    context = {'title':getTitle(), 'request': request,'form':nav}
    return render(request, 'pages/add.html', context)
    
def edit_nav(request,id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('pages:index'))
    nav = get_object_or_404(Nav, pk=id)
    if request.method == "POST":
        nav = NavForm(request.POST,instance=nav) # A form bound to the POST data
        if nav.is_valid(): # All validation rules pass
            new_nav = nav.save()
            return HttpResponseRedirect(reverse('pages:admin_list'))
    else:
        data={'title':nav.title,
            'url':nav.url,
            'position':nav.position,
        }
        nav = NavForm(data)
    context = {'title':getTitle(), 'request': request,'form':nav}
    return render(request, 'pages/add.html', context)

def delete_nav(request,id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('pages:index'))
    nav = get_object_or_404(Nav, pk=id)
    nav.delete()
    return HttpResponseRedirect(reverse('pages:admin_list'))
    
def delete_page(request,id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('pages:index'))
    page = get_object_or_404(Page, pk=id)
    page.delete()
    return HttpResponseRedirect(reverse('pages:admin_list'))
    
def test(request):
    context = {'title':getTitle(),'request': request}
    return render(request, 'pages/index.html', context)

