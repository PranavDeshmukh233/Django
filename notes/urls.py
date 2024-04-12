from django.urls import path
from . import views

urlpatterns=[
    path('notelist',views.NotesListView.as_view(),name="notelist"),
    path('note/<int:pk>',views.DetailView.as_view(),name="detail"),
    path('note/new',views.CreateView.as_view(),name="newnote")
]