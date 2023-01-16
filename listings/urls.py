from django.urls import path
from .views import *

urlpatterns = [
    path("", listing_list, name="listing_list"),
    path("<pk>/", listing_retrieve, name="listing_retrieve"),
    path("create", listing_create, name="listing_create"),
    path("update/<pk>/", listing_update, name="listing_update"),
    path("delete/<pk>/", listing_delete, name="listing_delete"),
]
