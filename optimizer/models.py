from django.db import models

class SQLFile(models.Model):
    uploaded_file = models.FileField(upload_to='uploads/')
    optimized_file = models.FileField(upload_to='optimized_files/', blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.uploaded_file.name
