from django.urls import path
from . import views

# Namespace for the learning_logs app
app_name = 'learning_logs'

# URL patterns for the learning log application
urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('topics/', views.topics, name='topics'),  # All topics
    path('topics/<int:topic_id>/', views.topic, name='topic'),  # Single topic detail
    path('new_topic/', views.new_topic, name='new_topic'),  # Add a new topic
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),  # Add a new entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),  # Edit an entry
]