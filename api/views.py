from django.http import JsonResponse

# Create your views here.


def home(request):
    return JsonResponse({'info': 'Django React App api', 'name': 'Sameer'})
