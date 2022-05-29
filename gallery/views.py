from django.shortcuts import render
from .models import Image
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404

# Create your views here.
def gallery(request):
    categories = Image.objects.distinct().values_list('category__name', flat=True)
    locations = Image.objects.distinct().values_list('location__name', flat=True)
    try:
        images = Image.objects.all()
    except ObjectDoesNotExist:
        raise Http404()
    return render(request, 'gallery.html', {'image': images, 'categories': categories, 'locations': locations})
