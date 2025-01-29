from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='HomePage'),
    path('add/', views.add_page, name='add_page'),
    path('save/', views.save_note, name='save_note'),
    path('edit/<int:note_id>/', views.edit_page, name='edit_page'),
    path('update/<int:note_id>/', views.update_note, name='update_note'),
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'),

]