import os
try:
    import django_filters
    from .models import *
except ModuleNotFoundError:
    os.system('pip install django-filter')



class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = filterstudent
        fields = '__all__'
