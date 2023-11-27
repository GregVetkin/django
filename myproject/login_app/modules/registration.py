from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from ..forms import LoginForm, RegisterForm

from django.db import connection


def registration(request):
    data = {"form": RegisterForm(),
            "message": ''}

    if request.method == "POST":
        login = request.POST.get("login")
        password_1 = request.POST.get("password_1")
        password_2 = request.POST.get("password_2")
        if password_1 != password_2:
            data['message'] = "Пароли не совпадают!"
            return render(request, "registration.html", data)

        if not _login_exists(login):
            create_new_user(login, password_1)
            #return HttpResponse(f"Пользователь {login} зарегистрирован!")
            return HttpResponseRedirect("login")
        else:
            data['message'] = "Пользователь уже существует!"
            return render(request, "registration.html", data)

    else:
        return render(request, "registration.html", {"form": RegisterForm()})



def _login_exists(login:str):
    with connection.cursor() as cursor:
        query = "SELECT EXISTS(SELECT login FROM my_schema.users WHERE login = %s);"
        data = (login,)
        cursor.execute(query, data)
        res = cursor.fetchone()[0]
    return res


def create_new_user(login, password):
    with connection.cursor() as cursor:
        query = "INSERT INTO my_schema.users (login, password) VALUES(%s, %s);"
        data = (login.lower(), password)
        cursor.execute(query, data)
