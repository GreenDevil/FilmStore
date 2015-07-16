from django.core.context_processors import csrf
from django.shortcuts import render_to_response, redirect
from films.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponse, Http404, HttpResponseRedirect
from films.forms import CommentForm, OrderForm

# Create your views here.

def films(request):
    return render_to_response('films.html', {'films': Film.objects.all()})

def film(request, films_id=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['film'] = Film.objects.get(id=films_id)
    args['comments'] = Comments.objects.filter(comments_film_id=films_id)
    args['form'] = comment_form
    return render_to_response('film.html', args)

def addcomment(request, films_id):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_film = Film.objects.get(id=films_id)
            form.save()
    return redirect('/films/get/%s/' % films_id)

def addorder(request):
    if request.POST:
        formo = OrderForm(request.POST)
        if formo.is_valid():
            # Process the data in formo.cleaned_data
            # ...
            return HttpResponseRedirect('/') # Redirect after POST
    else:
        formo = OrderForm() # An unbound formo

    return render_to_response('index.html', {
        'formo': formo,
    })