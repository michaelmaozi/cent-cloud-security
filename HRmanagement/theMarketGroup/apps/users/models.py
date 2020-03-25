from django.db import models
from datetime import datetime

from django.contrib.auth.models import AbstractUser

GENDER_CHOICES = (
    ("male", "male"),
    ("female", "female")
)


class BaseModel(models.Model):
    add_time = models.DateTimeField(default=datetime.now, verbose_name="added time")

    class Meta:
        abstract = True


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name="nick name", default="")
    birthday = models.DateField(verbose_name="birthday", null=True, blank=True)
    gender = models.CharField(verbose_name="gender", choices=GENDER_CHOICES, max_length=6)
    address = models.CharField(max_length=100, verbose_name="address", default="")
    mobile = models.CharField(max_length=11, verbose_name="mobil number")
    job_title = models.CharField(default="staff", verbose_name="job title", max_length=20,
                                choices=((0, "CEO"), (1, "manager"), (2, "sales"), (3, "delivery")))
    salary = models.FloatField(default=0.00, verbose_name="salary")
    work_years = models.CharField(max_length=20, verbose_name="working years")      

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = verbose_name


    def __str__(self):
        if self.nick_name:
            return self.nick_name
        else:
            return self.username # from AbstractUser








