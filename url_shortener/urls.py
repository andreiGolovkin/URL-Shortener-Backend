from django.urls import path

from url_shortener.requests import db_management_requests, sample_request, add_sample_link_request, navigate

urlpatterns = [
    path("/sample", sample_request.request, name="sample_request"),
    path("/add-sample-link", add_sample_link_request.request, name="add_sample_link"),
    path("/add", db_management_requests.make_new_record, name="add"),
    path("/summary", db_management_requests.get_summary, name="summary"),
    path("/r/<str:code>/", navigate.request, name="redirect"),
]
