from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class Qarzdorlar(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=17, blank=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('qarzdor', args=[str(self.id)])

class Qarzdor(models.Model):
    qarzdorlar = models.ForeignKey(Qarzdorlar, on_delete=models.CASCADE)
    product = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.qarzdorlar.name

    def get_absolute_url(self):
        return reverse('qarzdor', args=[str(self.qarzdorlar.id)])