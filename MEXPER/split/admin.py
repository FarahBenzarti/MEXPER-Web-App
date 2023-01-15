from django.contrib import admin
from .models import  events, Fixed, Variable, Saving

admin.site.register(events)
admin.site.register(Fixed)
admin.site.register(Variable)
admin.site.register(Saving)