from django.urls import path

from accounts.views import Banking
from accounts.views import Report
from accounts.views import Deposite
from accounts.views import Withdraw
from accounts.views import MyFirstClassBasedView
from django.contrib.auth.decorators import login_required


urlpatterns=[
    path('bank/', Banking),
    path('report/', Report),
    path('deposit/', Deposite),
    path('draw/', Withdraw),
    path('class/', MyFirstClassBasedView.as_view()),

]