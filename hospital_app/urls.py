from django.urls import path
from . import views

urlpatterns = [
    path('', views.HospitalListView.as_view(), name='list'),
    path('<int:pk>/', views.HospitalDetailView.as_view(), name='detail'),
    path('create/', views.HospitalCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.HospitalUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.HospitalDeleteView.as_view(), name='delete'),
    path('add_patient', views.PatientCreateView.as_view(), name='add_patient'),
]