from django.urls import path

from vendor import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.home_page, name='home'),
    path('POST/api/vendors/', views.VendorListCreate.as_view()),
    path('GET/api/vendors/<int:pk>/', views.VendorRetriveUpdate.as_view()),
    path('DELETE/api/vendors/delete/<int:pk>/', views.VendorRetriveDelete.as_view()),
    path('POST/api/purchase_orders/', views.PurchaseOrderListCreate.as_view()),
    path('GET/api/purchase_orders/<int:pk>/',views.PurchaseOrderRetriveUpdate.as_view()),
    path('DELETE/api/purchase_orders/delete/<int:pk>/',views.PurchaseOrderRetriveDelete.as_view()),
    path('GET/api/purchase_orders/<int:pk>/acknowledge/',views.AcknowledgeUpdate.as_view()),
    path('api/vendors/<int:pk>/performance/',views.VendorPerformance.as_view()),
    path('apitoken/', obtain_auth_token),
]
