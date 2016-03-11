from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .forms import db_form, testDbForm
from .models import testDb

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

    qry = """SELECT last_login, email, username from auth_user where id = 1"""
    # print qry
    cursor = settings.SQL.connect()
    rp = cursor.execute(qry)
    results = rp.fetchall()
    # print results
    # print results[0]

    msg = "Welcome"
    context = {
        "msg": msg,
        "results": results[0],
    }


    return render(request, "dashboard.html", context)

def testDb_create(request):
    form = testDbForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    msg = "create"
    context = {
        "msg": msg,
        "form": form,
    }
    return render(request, "testDb.html", context)

def testDb_detail(request, id):
    # instance = testDb.objects.get(id=1) ## returns error if not found
    instance = get_object_or_404(testDb, id=id)
    msg = "detail"
    context = {
        "msg": msg,
        "instance": instance,
    }
    return render(request, "testDb.html", context)

def testDb_list(request):
    queryset = testDb.objects.all()
    msg = "list"
    context = {
        "object_list": queryset,
        "msg": msg,
    }
    print"wtf"
    return render(request, "testDb.html", context)

def testDb_update(request):
    msg = "update"
    context = {
        "msg": msg,
    }
    return render(request, "testDb.html", context)

def testDb_delete(request):
    msg = "delete"
    context = {
        "msg": msg,
    }
    return render(request, "testDb.html", context)