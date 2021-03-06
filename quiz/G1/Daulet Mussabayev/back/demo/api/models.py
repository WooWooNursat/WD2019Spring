from django.db import models
from django.contrib.auth.models import User

class ContactManager(models.Manager):
    def for_user_order_by_name(self, user):
        return self.filter(created_by=user).order_by('name')

class Contact(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=2)

    objects = ContactManager()
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone
        }
    def __str__(self):
        return '{}: {}'.format(self.id,self.name, self.phone)

