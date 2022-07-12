from django.db import models
from courses_app.models import Course


class Student(models.Model):
    first_name = models.CharField(max_length=100, default="name")
    last_name = models.CharField(max_length=100, default="last name")
    date_of_birth = models.DateField()
    email = models.EmailField(default="mail@gmail.com")
    phone_number = models.CharField(max_length=13, null=True)
    description = models.TextField(null=True)
    FEMALE = 'F'
    MALE = 'M'
    GENDER_CHOICES = [
        (FEMALE, 'female'),
        (MALE, 'male')
    ]
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default=MALE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name

    #
    # def save(self,*args,**kwargs):
    #     # for field_name in ['first_name','last_name']:
    #     #     val = getattr(self,field_name,False)
    #     #     if val:
    #     #         setattr(self,field_name,val.capitalize())
    #     # super(Student,self).save(*args,**kwargs)

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()
        super(Student,self).save()


