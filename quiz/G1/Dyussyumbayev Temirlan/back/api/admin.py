from django.contrib import admin
from api.models import Contacts
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token

# Register your models here.

admin.site.register(Contacts)