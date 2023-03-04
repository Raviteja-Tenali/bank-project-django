from django.urls import path

from transactions.views import Register


urlpatterns = [

    path('reg/', Register),
]