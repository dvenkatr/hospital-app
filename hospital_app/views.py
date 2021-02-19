from django.shortcuts import render
from django.views.generic import (View, TemplateView, 
                                    ListView, DetailView,
                                    CreateView, UpdateView, DeleteView)
                        
from hospital_app import models

from django.urls import reverse_lazy

from hospital_app.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.mixins import LoginRequiredMixin


def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False) # create user object from user form object
            user.username = user.email
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request, "register.html", {"user_form" : user_form, "registered" : registered})


def user_login(request):
    logged_in = False
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        username = email
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried to login with username: {} and failed".format(email))
            return HttpResponse("Invalid login details")
    else:
        return render(request, "login.html")


@login_required
def user_logout(request):
    logout(request)
    return render(request, "logout.html")


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["welcome_message"] = "Welcome!"
        return context

class HospitalListView(ListView):
    context_object_name = "hospitals"
    model = models.Hospital
    # default template = hospital_list.html

class HospitalDetailView(DetailView):
    model = models.Hospital
    template_name = "hospital_app/hospital_detail.html"

class HospitalCreateView(LoginRequiredMixin, CreateView):
    fields = "__all__"
    model = models.Hospital

class HospitalUpdateView(LoginRequiredMixin, UpdateView):
    fields = ("hospital_name", "admin")
    model = models.Hospital

class HospitalDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Hospital
    success_url = reverse_lazy("list")

class PatientCreateView(LoginRequiredMixin, CreateView):
    fields = "__all__"
    model = models.Patient
    template_name = "hospital_app/add_patient.html"
    # initial = {'hospital' : 3}
    def get_initial(self):
        initial = super().get_initial()
        initial["hospital"] = self.request.GET["hospital_id"]
        return initial