from django.contrib import admin

from first_app.models import * ## import all models

# Register your models here.

## run 'python manage.py createsuperuser' to create super-user

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)