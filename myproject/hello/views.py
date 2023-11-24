from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder


def set(request):
    username = request.GET.get("username", "Undefined")

    response = HttpResponse(f"Hello {username}")

    response.set_cookie("username", username)
    return response



def get(request):
    username = request.COOKIES.get("username", "Undefined")
    return HttpResponse(f"Hello {username}")




def index(request):
    header = "User data"
    lang = ["Python", "Docker", "PyQt", "Git"]
    user = {"name": "Gregory", "age": 26, "familyname": "Vetkin"}
    address = ("Moscow", "Studencheskaya street", 21, 31)

    data = {"header": header,
            "lang": lang,
            "user": user,
            "address": address}

    return render(request, "index.html", context=data)