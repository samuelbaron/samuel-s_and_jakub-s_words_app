from django.urls import path
from . import views


app_name = 'words_manager'
urlpatterns = [
    path('all/', views.sets_display, name='sets_display'),
    path('add/', views.set_add, name='set_add'),
    path('<int:set_id>/', views.set_display, name='set_display'),

    #path('<int:set_id>/edit/', views.set_edit, name='set_edit'),
    #path('<int:set_id>/add/', views.word_add, name='word_add'),
    #path('<int:set_id>/<int:word_id>/edit/', views.word_edit, name='word_edit'),
]