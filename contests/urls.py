from django.urls import path, include
from contests.views import con

urlpatterns = [
    path('', con, name='con'),

]