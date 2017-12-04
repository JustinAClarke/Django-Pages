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
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib import messages
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
import datetime

# Create your views here.

from .models import Page
from .forms import *

def getTitle(title=False):
    if(title):
        return getTitle() + " - " + title
    else:
        return "Justin Fuhrmeister-Clarke"

def multiLineStr(string):
    string = "<br />".join(string.split("\n"))
    #return string.replace("\n","<br>\n")
    return string

def rev_multiLineStr(string):
    string = "\n".join(string.split("<br />"))
    #return string.replace("\n","<br>\n")
    return string
    

def index(request):
    context = {'title':getTitle(),'request': request}
    return render(request, 'pages/index.html', context)

def admin_list(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('photos:index'))
    pages = Page.objects.all().order_by('title')
    navs = Nav.objects.all().order_by('title')
    contacts = Contact.objects.all().order_by('id')


    context = {'title':getTitle(), 'request': request,'pages':pages,'navs':navs, 'contacts':contacts}
    return render(request, 'pages/admin_list.html', context)




def add_page(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('pages:index'))
    if request.method == "POST":
        page = PageForm(request.POST) # A form bound to the POST data
        if page.is_valid(): # All validation rules pass
            new_page = page.save()
            new_page.content=multiLineStr(new_page.content)
            new_page.save()
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
            new_page.content=multiLineStr(new_page.content)
            new_page.save()

            return HttpResponseRedirect(reverse('pages:admin_list'))
    else:
        data={'title':page.title,
            'url':page.url,
            'content':rev_multiLineStr(page.content),
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
    
    
    
def contact(request):
    if request.method == "POST":
        contact = ContactForm(request.POST) # A form bound to the POST data
        if contact.is_valid(): # All validation rules pass
            new_contact = contact.save()
            new_contact.note=multiLineStr(new_contact.note)
            new_contact.save()

            #send email
            context = {
                'time': datetime.datetime.now().isoformat(),
                'name': contact.cleaned_data['name'],
                'subject': contact.cleaned_data['subject'],
                'email': contact.cleaned_data['email'],
                'phone': contact.cleaned_data['phone'],
                'note': multiLineStr(contact.cleaned_data['note']),
            }
            message = render_to_string('pages/email.html', context)
            return_message = render_to_string('pages/email_sender.html', context)
            #send client email
            try:
                send_mail("Contact Us Form Submitted", return_message, "info@justin.fuhrmeister-clarke.com", [contact.cleaned_data['email']])
            except BadHeaderError:
                messages.add_message(request, messages.ERROR, 'form Submission Failed')

            #send my email
            try:
                send_mail("Website Contact Us", message, "website@justin.fuhrmeister-clarke.com", ['info@justin.fuhrmeister-clarke.com'])
            except BadHeaderError:
                messages.add_message(request, messages.ERROR, 'form Submission Failed')
                return HttpResponseRedirect(reverse('pages:contact'))
                #return HttpResponse('Invalid header found.')
            
            messages.add_message(request, messages.INFO, 'Form submission success')
            return HttpResponseRedirect(reverse('pages:index'))
    else:
        contact = ContactForm()
    context = {'title':getTitle('Contact'), 'request': request,'form':contact}
    return render(request, 'pages/contact.html', context)


def contact_list(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('pages:index'))
    contacts = Contact.objects.all().order_by('id')
    context = {'title':getTitle(), 'request': request,'contacts':contacts}
    return render(request, 'pages/contact_list.html', context)
    
    
def contact_view(request,id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('pages:index'))
    contact = get_object_or_404(Contact, pk=id)
    context = {'title':getTitle(), 'request': request,'contact':contact}
    return render(request, 'pages/contact_view.html', context)
    
def contact_delete(request,id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('pages:index'))
    contact = get_object_or_404(Contact, pk=id)
    contact.delete()
    return HttpResponseRedirect(reverse('pages:contact_list'))

def test(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('pages:index'))
    context = {'title':getTitle(),'request': request}
    return render(request, 'pages/index.html', context)

