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
from django.forms import ModelForm
from .models import Nav, Page



class PageForm(ModelForm):
    class Meta:
        model = Page
        fields = '__all__'
        #fields = [ 'Title' ]

class NavForm(ModelForm):
    class Meta:
        model = Nav
        fields = '__all__'
        #fields = [ 'Title' ]
