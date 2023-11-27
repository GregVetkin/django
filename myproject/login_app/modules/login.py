from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from ..forms import LoginForm, RegisterForm


from django.db import connection


def login(request):
    data = {"form": LoginForm(),
            "message": ''}
    if request.method == "POST":
        login = request.POST.get("login")
        password = request.POST.get("password")

        if correct_login(login, password):
            return HttpResponse(f"Добро пожаловать, {login}!")
        else:
            data['message'] = 'Неверный логин или пароль!'
            return render(request, 'login.html', context=data)

    else:
        return render(request, "login.html", context=data)


def correct_login(login, password):
    with connection.cursor() as cursor:
        query = "SELECT EXISTS(SELECT login, password FROM my_schema.users WHERE login = %s AND password = %s);"
        data = (login, password)
        cursor.execute(query, data)
        res = cursor.fetchone()[0]
    return res
