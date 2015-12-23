from django.template.response import TemplateResponse

def blog_index(request):
    return TemplateResponse(request, 'home.html')