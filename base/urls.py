from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    )

urlpatterns = [
    path('', views.endpoints),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('advocates/', views.advocates_list, name='advocates'),
    
#     path('advocates/<str:username>', views.advocate_detail)#
    path('advocates/<str:username>', views.AdvocateDetail.as_view()),
    

    path('companies/', views.companies_list),

    
]
