from django.urls import path
from .views import BookAPIView , BookAPIViewALL

urlpatterns = [
    path("", BookAPIView.as_view(), name = "book_list"),
    path("getALL", BookAPIViewALL.as_view(), name = "book_list_all"),
]
