from django.conf import settings
from django.shortcuts import render

from .forms import db_form

# Create your views here.
def home(request):

    msg = "Welcome"
    context = {
        "msg": msg,
    }

    return render(request, "home.html", context)

def db(request):

    msg = "Welcome"
    show_form = True

    form = db_form(request.POST or None)

    context = {
        "msg": msg,
        "show_form": show_form,
        "form": form,
    }

    if form.is_valid():
        form.save()
        msg = "Thank you for registering!"
        show_form = False
        context = {
            "msg": msg,
            "show_form": show_form,
        }

    return render(request, "db.html", context)

def dashboard(request):

    qry = """SELECT name from django_site where id = 1"""
    print qry
    cursor = settings.SQL.connect()
    rp = cursor.execute(qry)
    results = rp.fetchall()
    print results
    print results[0]

    msg = "Welcome"
    context = {
        "msg": msg,
        "results": results[0],
    }


    return render(request, "dashboard.html", context)