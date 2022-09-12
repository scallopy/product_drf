from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('drinks/', views.drink_list),
    path('drinks_list/', views.list_drink),
    path('drinks_list/<int:id>', views.drink_detail)
]


# to recieve json: http://127.0.0.1:8000/api_drinks/drinks_list.json
# http://127.0.0.1:8000/api_drinks/drinks_list/2.json
urlpatterns = format_suffix_patterns(urlpatterns)
