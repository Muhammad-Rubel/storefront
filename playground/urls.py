from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('hello/', views.say_hello),
    path('with-id/<int:id>', views.with_id),
    path('with-query/', views.with_query),
    path('with-html-template/', views.with_html_template),
    path('with-template-context/', views.with_template_context)
]