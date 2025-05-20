from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_list, name='service_list'),        # ← overview page
    path('visa/', views.visa_service, name='visa_service'),
    path('passport/', views.passport_service, name='passport_service'),
    path('consular/', views.consular_assistance, name='consular_assistance'),
    path('trade/', views.trade_investment, name='trade_investment'),
]
