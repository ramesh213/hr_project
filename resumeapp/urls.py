from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('show',views.ShowView.as_view(), name= 'show'),
    path('<int:id>',views.CandidateView.as_view(), name = 'candidate')
]