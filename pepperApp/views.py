from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import db_form, testDbForm
from .models import testDb


def home(request):

    msg = "Welcome"
    context = {
        "msg": msg,
    }

    return render(request, "home.html", context)


def diary(request):

    msg = "Plant Diary"
    context = {
        "msg": msg,
    }

    return render(request, "diary.html", context)


# Sample Views (Remove once they are no longer needed)
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
        messages.success(request, "New Record Created!")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Not Created.")

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

def testDb_update(request, id):
    instance = get_object_or_404(testDb, id=id)
    form = testDbForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Record Updated!")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Not Updated.")

    msg = "update"
    context = {
        "msg": msg,
        "instance": instance,
        "form": form,
    }
    return render(request, "testDb.html", context)

def testDb_delete(request, id):
    instance = get_object_or_404(testDb, id=id)
    instance.delete()
    messages.success(request, "Record Deleted!")
    return redirect('list')