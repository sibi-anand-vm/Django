from django.db import models
class File(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    username=models.CharField(max_length=50)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=150)
    state=models.CharField(max_length=50)
    pincode=models.IntegerField()
    def __str__(self):
        return(f"{self.username}")