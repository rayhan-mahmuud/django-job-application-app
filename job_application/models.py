from django.db import models


class JobForm(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()
    occupation = models.CharField(max_length=80)
    city = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.date} - {self.first_name} {self.last_name}"


class UserMessage(models.Model):
    user_name = models.CharField(max_length=80)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.user_name}: {self.subject} - {self.email}"