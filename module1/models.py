from django.db import models

class Register(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(primary_key=True)
    password=models.CharField(max_length=100)
    phonenumber=models.PositiveBigIntegerField()
    class Meta:
        db_table="Register"

class Feedback(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(primary_key=True)
    comment=models.TextField(max_length=216)
    class Meta:
        db_table="Feedback"