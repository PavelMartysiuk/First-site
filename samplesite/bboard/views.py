from django.shortcuts import render, redirect
from .models import Bd, Rubric
from django.views.generic.edit import CreateView
from .forms import BdForm
from django.urls import reverse_lazy
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.template.context_processors import csrf

User = get_user_model()


# Create your views here.
def index(request):
    bbs = Bd.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}

    return render(request, 'index.html', context)


def by_rubric(request, rubric_id):
    # print(rubric_id)
    bbs = Bd.objects.filter(rubric=rubric_id)
    # for bb in bbs:
    #   print(bb.title,bb.content)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'by_rubric.html', context)


class BdcreateView(CreateView):
    template_name = 'create.html'
    form_class = BdForm
    success_url = '/bboard/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


def sign_up(request):
    if not request.POST:
        response = csrf(request)
        response['path'] = '/bboard/sign_up/'
        response['title'] = 'sign_up'
        return render(request, 'form.html', response)
    else:
        login = request.POST['uname']
        pswd = request.POST['pswd']
        usr = User(username=login, password=pswd)
        usr.save()
        auth.login(request, usr)
        return redirect('/bboard/')


def login(request):
    response = csrf(request)
    response['path'] = '/bboard/login/'
    response['title'] = 'login'
    if not request.POST:
        return render(request, 'form.html', response)
    else:
        login = request.POST['uname']
        pswd = request.POST['pswd']
        user = auth.authenticate(password=pswd, username=login)
        if not user:
            try:
                user = User.objects.get(username=login, password=pswd)
            except:
                user = None
        if user:
            auth.login(request, user)
            return redirect('/bboard/')
        else:
            response['error'] = "user doesn't exist"
            return render(request, 'form.html', response)


def logout(request):
    auth.logout(request)
    return redirect('/bboard/')
