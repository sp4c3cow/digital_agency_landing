from django.db import models

class ContactForm(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=200)
    message = models.TextField(max_length=600)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name