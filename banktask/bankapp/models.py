from django.db import models

# Create your models here.
class District(models.Model):
    district = models.CharField(max_length=100)
    def __str__(self):
        return self.district
class Branch(models.Model):
    distid = models.ForeignKey(District, on_delete=models.CASCADE)
    branch = models.CharField(max_length=100)
    def __str__(self):
        return self.branch

class ProcessData(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField()
    age=models.IntegerField()
    gender=models.CharField(max_length=20)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    address=models.TextField()

    def __str__(self):
        return ("{} dob-{} gender-{}".format(self.name,self.dob,self.gender))
