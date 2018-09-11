from django.contrib import admin
from .models import Like
from .models import User
from .models import Flix

admin.site.register(User)
admin.site.register(Flix)
admin.site.register(Like)
# Register your models here.
