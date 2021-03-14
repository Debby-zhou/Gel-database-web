from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30, blank=False, null=False, verbose_name="username", default="debby")
    email = models.EmailField(blank=False, null=False, verbose_name="email", default="debby940406@gmail.com")
    password = models.CharField(max_length=30, blank=False, null=False, verbose_name="password",default="qaz123456789")

    def __str__(self):
        return "welcome %s" % self.username
    class Meta:
        app_label = "welcome"
