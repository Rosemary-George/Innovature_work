from django.urls import path
from . import views
from fileApi.views import FileUploadAPIView,download_file

urlpatterns = [
    path('upload-file/', FileUploadAPIView.as_view(), name='upload-file'),
    path('download/<int:id>/', views.download_file, name='download-file'),
]

