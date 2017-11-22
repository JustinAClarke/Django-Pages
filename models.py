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
from django.db import models

# Create your models here.


class Page(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=128,unique=True)
    content = models.TextField()
    
    def __str__(self):
        return self.title

class Nav(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=128)
    position = models.IntegerField(unique=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=256)
    subject = models.CharField(max_length=256)
    email = models.CharField(max_length=128,null=True)
    phone = models.CharField(max_length=128,null=True)
    note = models.TextField()
    date = models.DateTimeField('Date',auto_now=True)

    def __str__(self):
        return self.id


