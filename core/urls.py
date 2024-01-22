from django.urls import path

from core.views import BookListView

urlpatterns = [

    path('', BookListView.as_view(), name='home')
]