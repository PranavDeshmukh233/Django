from django.shortcuts import render
from django.http import Http404
from .models import notes
from django.views.generic import ListView,DeleteView
# Create your views here.
# def list(request):
#     all_notes=notes.objects.all()
#     return render(request,'notes/noteslist.html',{'notes':all_notes})

# def detail(request,pk):
#     try:
#         note=notes.objects.get(pk=pk)
#     except notes.DoesNotExist:
#         raise Http404("Note does not eixst")
    
#     return render(request,'notes/detail.html',{'note':note})

class NotesListView(ListView):
    template_name='notes/noteslist.html'
    model = notes
    context_object_name= "notes"

class DetailView(DeleteView):
    template_name="notes/detail.html"
    model=notes
    context_object_name="note"
