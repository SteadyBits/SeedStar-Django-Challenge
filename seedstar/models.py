from django.db import models

# SQLite database model below, with attribute for each field
class Contact(models.Model):
    fname = models.CharField(max_length = 30, blank=False)
    lname = models.CharField(max_length = 30, blank=False)
    email_address = models.EmailField(max_length=50, blank=False, unique=True)

