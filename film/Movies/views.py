from django.shortcuts import render
from Movies.models import Movie
from Movies.forms import Movieform
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# def home(request):
#     m = Movie.objects.all()
#     return render(request, 'home.html',{'m':m})

#CLASS BASED CODE
class movieListview(ListView):
    model=Movie
    template_name="home.html"
    context_object_name="m"

# def addfilm(request):
#     if (request.method == "POST"):
#         t = request.POST['t']
#         y = request.POST['y']
#         r =  request.Post['r']
#         d = request.POST['d']
#         i = request.FILES['i']
#         m = Movie.objects.create(title=t, year=y, rating=r ,desc=d, img=i)
#         m.save()
#         return home(request)
#     return render(request,'addfilm.html')

class createview(CreateView):
    model=Movie
    template_name="addfilm.html"
    fields=['title','year','rating','desc','img']
    success_url = reverse_lazy('Movies:home')


# def viewdetails(request,p):
#     m = Movie.objects.get(id=p)
#     return render(request,'viewdetails.html',{'m':m})

class  Moviedetailview(DetailView):
    model=Movie
    template_name="viewdetails.html"
    context_object_name='m'

# def deletemovie(request,p):
#
#     m = Movie.objects.get(id=p)
#     m.delete()
#     return home(request)

class  deleteview(DeleteView):
    model=Movie
    template_name="deletemovie.html"
    success_url = reverse_lazy('Movies:home')

# def editmovie(request,p):
#     m = Movie.objects.get(id=p)
#     form = Movieform(instance=m)
#     if (request.method == "POST"):
#         form = Movieform(request.POST,request.FILES,instance=m)
#
#         if form.is_valid():
#             form.save()
#             return home(request)
#     return render(request, 'editmovie.html', {'form': form})
class updateview(UpdateView):
    model=Movie
    template_name="editmovie.html"
    fields=['title','year','rating','desc','img']
    success_url = reverse_lazy('Movies:home')