from django.http import HttpResponse


def home_page(request):
    return HttpResponse("<html><head><title>Blog</title><body>Hello</body></html>")
