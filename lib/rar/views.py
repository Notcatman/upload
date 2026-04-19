from django.shortcuts import render, get_object_or_404
from .models import Photo

def photo(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    return render(request, 'images.html', {'photo': photo})