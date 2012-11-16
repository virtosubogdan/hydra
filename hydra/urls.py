from django.conf.urls.defaults import patterns, url
from hydra import views

urlpatterns = patterns(
    '',
    url(r"^$", views.index, name="index"),
    url(r"login/$", "django.contrib.auth.views.login",
        {"template_name": "login/login.html",
         "redirect_field_name": "index"},
        name="login"),
    url(r"logout/$", views.logout, name="logout"),
    url(r"tickets/$", views.tickets, name="tickets"),

)
