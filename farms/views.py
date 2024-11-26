from django.shortcuts import render


def home(request):

    context = {'title':'home'}
    return render(request, "farms/home.html", context)

