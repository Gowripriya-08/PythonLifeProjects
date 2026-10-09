from django.db import models

# Create your models here.
class students(models.Model):
    name = models.CharField(max_length =100)
    rollnumber = models.IntegerField(unique=True)
    student_class = models.CharField(max_length =50 )
    age = models.IntegerField()
    parent_contact = models.CharField(max_length=15)

    def _str_(self):
      return f"{self.rollnumber}-{self.name}"
