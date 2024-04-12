from django.urls import path
from . import views

urlpatterns=[
    path('notelist',views.NotesListView.as_view(),name="notelist"),
    path('note/<int:pk>',views.DetailView.as_view())
]