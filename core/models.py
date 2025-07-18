from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

class Banner(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='banners/')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
