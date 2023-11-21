from django.http import HttpResponse

def index(request):
    '''Index view'''
    return HttpResponse("<h2>Hello World</h2>")