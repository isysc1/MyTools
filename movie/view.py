"""
Created by Young on 2020/1/11 9:48
"""
from django.shortcuts import render
from .models import Information


def movie(request):
    movieInformation = Information.objects.all()
    return render(request, "movie.html", {'information': movieInformation})


def set(request):
    if request.method == "GET":
        return render(request, "movie.html")
    else:
        newInformation = Information()
        InputMovieName = request.POST.get('InputMovieName')
        ImagesUrl = request.POST.get('InputImagesUrl')
        ImagesUrl2 = request.POST.get('InputImagesUrl2')
        InputTime = request.POST.get('InputTime')
        InputScore = request.POST.get('InputScore')
        InputEstimate = request.POST.get('InputEstimate')
        InputType = request.POST.get('InputType')
        newInformation.name = InputMovieName
        newInformation.image_Url1 = ImagesUrl
        newInformation.image_Url2 = ImagesUrl2
        newInformation.time = InputTime
        newInformation.score = InputScore
        newInformation.reviews = InputEstimate
        newInformation.kind = InputType
        newInformation.save()
    return render(request, "movieAdmin.html")
