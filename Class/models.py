from django.db import models
from datetime import datetime,date
import uuid
# Create your models here.

class NameField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(NameField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()

class Subject(models.Model):
    name = models.CharField(max_length=50,null=True)
    class Meta:
        db_table = 'SUBJECT'

    def __str__(self) -> str:
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100,null=True)
    class Meta:
        db_table = 'COURSE'

    def __str__(self) -> str:
        return self.name


class Student(models.Model):
    STATUS = (
        ('understudies','understudies'),
        ('complete','complete'),
        ('resign','resign'),
    )
    roll_id = models.CharField(max_length=10, unique=True)
    status = models.CharField(max_length=100,
                                choices=STATUS,
                                default='understudies')
    
    student = NameField(max_length=50,null=True)
    guardian = NameField(max_length=50,null=True)
    phone = models.CharField(max_length=50,null=True)
    guardian_ph = models.CharField(max_length=50,null=True)
    email = models.EmailField(null=True)
    address = models.CharField(max_length=50,null=True)

    subjects = models.ManyToManyField(Subject)
    course = models.ForeignKey(Course,null=True,on_delete=models.SET_NULL)

    date_created = models.DateTimeField(auto_now_add=True,null=True)


    class Meta:
        db_table = 'STUDENT'

    def generate_roll_id(self):
        first_part = str(uuid.uuid4()).split('-')[0]
        return first_part

    def __str__(self) -> str:
        return self.student


class Query(models.Model):
    roll_id = models.CharField(max_length=10, unique=True)
    student = NameField(max_length=50,null=True)
    guardian = NameField(max_length=50,null=True)
    phone = models.CharField(max_length=50,null=True)
    subjects = models.ManyToManyField(Subject)
    course = models.ForeignKey(Course,null=True,on_delete=models.SET_NULL)

    date_created = models.DateTimeField(auto_now_add=True,null=True)

    class Meta:
        db_table = 'QUERY'

    def generate_roll_id(self):
        first_part = str(uuid.uuid4()).split('-')[0]
        return first_part
    
    def __str__(self) -> str:
        return self.student


class filterstudent(models.Model):
    STATUS = (
        ('understudies','understudies'),
        ('complete','complete'),
        ('resign','resign'),
    )
    status = models.CharField(max_length=100,
                                choices=STATUS,
                                default='understudies')
    student = models.ForeignKey(Student,null=True,on_delete=models.SET_NULL)
    course = models.ForeignKey(Course,null=True,on_delete=models.SET_NULL)
    

    class Meta:
        db_table = 'FILTERSTUDENT'
