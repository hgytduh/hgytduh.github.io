from django.shortcuts import render


def home(request):
	context = {}
	template = "index.html"
	return render(request, template,context)

def forums(request):
	context = {}
	template = "forums.html"
	return render(request, template, context)