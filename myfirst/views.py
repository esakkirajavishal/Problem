from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    params = {'name':'sadhana', 'place':'india'}
    return render(request, "index.html", params)

def about(request):
    return HttpResponse('''<a href="https://stackoverflow.com/questions/68100026/django-syntaxerror">Google</a>
    <br><a href='/'>back<a>''')
