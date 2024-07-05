from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Playground index.")

def say_hello(request):
    return HttpResponse("Hello page.")

# url with id parameter
def with_id(request, id):
    return HttpResponse("With id -  " + str(id))

# url with query parameters
def with_query(request):
    name = request.GET.get('name', '')

    # if name is not provided
    if name == '':
        return HttpResponse("No name provided.")
    else:
        return HttpResponse("Name is - " + name)

def with_html_template(request):
    return render(request, 'with_html_template.html')

def with_template_context(request):
    context = {
        'name': 'John Doe',
        'age': 30,
        'city': 'New York'
    }
    return render(request, 'with_template_context.html', context)
