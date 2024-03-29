from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForms

# Create your views here.


def home(request):
    obj = Movie.objects.all()
    return render(request, 'home.html', {'movies': obj})


def details(request, movie_id):
    movies = Movie.objects.get(id=movie_id)
    return render(request, 'details.html', {'movie_list': [movies]})



def add(request):
    if request.method == 'POST':
        form = MovieForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = MovieForms()

    return render(request, 'add.html', {'form': form})

def update(request, id):
    movie = Movie.objects.get(id=id)
    form = MovieForms(request.POST or None, request.FILES, instance=movie)

    if form.is_valid():
        form.save()

        return redirect('/')
    return render(request, 'update.html', {'form': form, 'movie': movie})


def delete(request, id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')

    return render(request, 'delete.html')



