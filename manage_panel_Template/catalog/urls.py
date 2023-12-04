from django.urls import path
from .views import *


urlpatterns = [
    path('', catalog_page),
    path('add_comment/', add_comment_page),
    path('thanks/', thanks_page, name="thanks_page"),
    path('feedback_success/', feedbacks_page, name="feedbacks_page"),
    path('add_review/', add_comment_fitbacks_page, name="add_comment_fitbacks_page")
]