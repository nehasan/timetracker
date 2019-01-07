from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Attendance(models.Model):
    user = models.ForeignKey(User, related_name='attendances', on_delete = models.CASCADE)
    check_in_at = models.TimeField(null = true)
    check_out_at = models.TimeField(null = true)
    total_time_in_sec = models.IntegerField(default = 0)
    status = models.CharField(max_length = 255)
