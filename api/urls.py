from django.urls import path, include
from rest_framework import routers

from .views import PartView, LineView, LineDataView, SpareView, Sub_AssemblyView

routers = routers.DefaultRouter()
routers.register(r'part', PartView, 'Part')
routers.register(r'line', LineView, 'Line')
routers.register(r'linedata', LineDataView, 'Linedata')
routers.register(r'spare', SpareView, 'Spare')
routers.register(r'sub_assembly', Sub_AssemblyView, 'Sub_Assembly')

urlpatterns = [
    path('api/', include(routers.urls))
]