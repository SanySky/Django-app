from django.urls import path

from .views import process_det_view, user_form, handle_file_upload

app_name = "requestdataapp"

urlpatterns = [
    path("get/", process_det_view, name="get-vew"),
    path("bio/", user_form, name="user-form"),
    path("upload/", handle_file_upload, name="file-upload"),
]


