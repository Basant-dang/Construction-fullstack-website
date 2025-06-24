from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)
    client_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=[
        ('Planned', 'Planned'),
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ])
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name



class Document(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='documents')
    file = models.FileField(upload_to='project_documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255, default=True)

    def __str__(self):
        return self.file.name
