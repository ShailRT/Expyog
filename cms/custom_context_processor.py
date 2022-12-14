from .models import Service

def service_renderer(request):
    return {
       'all_services': Service.objects.all() ,
    }