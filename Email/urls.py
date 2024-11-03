from django.urls import path
from . import views

urlpatterns = [
    path('Get_emails/',views.get_email),
    path('Add_Email/',views.add_email),
    path('send_email/',views.Send_Email)
]
