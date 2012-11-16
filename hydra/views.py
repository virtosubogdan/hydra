import django.contrib.auth
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import hydra.models as models


def index(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("login")
    return HttpResponse("Welcome Trevira")


def logout(request):
    django.contrib.auth.logout(request)
    return HttpResponseRedirect("/login")


@login_required
def tickets(request):
    return HttpResponse("List tickets")


@login_required
def my_tickets(request):
    tickets = models.Ticket.objects.filter(requester=request.user)


@login_required
def ticket(request):
    pass
