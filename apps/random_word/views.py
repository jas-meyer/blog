from django.shortcuts import render,HttpResponse, redirect
from django.utils.crypto import get_random_string
def index(request):

	return render(request, 'random_word/index.html')
def create(request):
	if 'counter' in request.session:
		request.session['counter'] += 1
	else: 
		request.session['counter'] = 0
	request.session['genword'] = get_random_string(length=14)

	return redirect('/random_word')
def reset(request):
	request.session['counter'] = 0
	return redirect('/random_word')

# Create your views here.
