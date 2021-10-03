from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def _str_(self):
        return self.title


    def get_absolute_url(self):
        return reverse('Post-Details', kwargs={'pk': self.pk})

class InspectionList(models.Model):
    waferId = models.CharField(max_length=100)
    waferNo = models.TextField()
    lotId = models.CharField(max_length=100)
    lotNo = models.TextField()
    testId = models.CharField(max_length=100)
    testNo = models.TextField()
    defectId = models.CharField(max_length=100)
    defectNo = models.TextField()

    # content = models.TextField()
    # date_posted = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    def _str_(self):
        return self.id