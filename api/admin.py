from django.contrib import admin
from django.contrib.auth.models import Group
from .models import CandidateInfo
admin.site.unregister(Group)
# Register your models here.
admin.site.register(CandidateInfo)