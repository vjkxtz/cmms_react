from django.contrib import admin
from .models import Part, Line, LineData, Spare, Sub_Assembly
# Register your models here.

admin.site.register(Part)
admin.site.register(Line)
admin.site.register(LineData)
admin.site.register(Spare)
admin.site.register(Sub_Assembly)