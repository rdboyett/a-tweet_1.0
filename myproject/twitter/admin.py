from django.contrib import admin
from myproject.twitter.models import *


admin.site.register(UserInfo)
admin.site.register(Classroom)
admin.site.register(Tweet)
admin.site.register(HashTag)