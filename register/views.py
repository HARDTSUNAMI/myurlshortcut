from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import F
from django.http import HttpRequest
from django.shortcuts import HttpResponse, redirect, render
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from django.views.generic import DeleteView
from .forms import LoginForm, LinkForm
from .models import LinkModel
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

"""РЕГИСТРАЦИЯ"""


def register_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile')
        return render(request, 'register/registr.html', {'form': form})
    form = UserCreationForm()
    return render(request, 'register/registr.html', {'form': form})


"""АВТОРИЗАЦИЯ"""


def auth_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = LoginForm({'username': request.POST['username'],
                          'password': request.POST['password']
                          })
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password']
                                )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('main')
                else:
                    return HttpResponse('Неправильно указан пароль или имя пользователя')
            else:
                return HttpResponse('Неправильно указан пароль или имя пользователя')
    else:
        form = LoginForm()
    return render(request, 'register/login.html', {'form': form})


"""ДЛЯ НЕЗАРЕГ ПОЛЬЗОВ"""


@csrf_protect
def profile_view(request: HttpRequest) -> HttpResponse:
    form = LinkForm()
    data = {
        'form': form,
    }

    if request.method == 'POST':
        form = LinkForm(request.POST.dict())
        if form.is_valid():
            form.save()
            return redirect('newlink/')
        else:
            data = {'form': form}
            return render(request, 'register/profile.html', data)

    return render(request, 'register/profile.html', data)


"""ДЛЯ ЗАРЕГ ПОЛЬЗОВ"""


@login_required(login_url='auth/')
def mainpage_view(request: HttpRequest) -> HttpResponse:
    form = LinkForm()
    data = {
        'form': form,
    }
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = LinkForm(request.POST.dict())
        if form.is_valid():
            instance = form.save(commit=True)
            instance.author = request.user
            instance.save()
            return redirect('/newlink/')
        else:
            data = {'form': form}
    return render(request, 'register/mainpage.html', data)


"""ПЕРЕЧЕНЬ СГЕНЕРИРОВАННЫХ ССЫЛОК ДЛЯ ПОЛЬЗОВАТЕЛЯ"""


@login_required()
def pagination_view(request: HttpRequest) -> HttpResponse:
    slug = LinkModel.objects.filter(author=request.user)
    page = request.GET.get('page', 1)
    paginator = Paginator(slug, 3)

    try:
        slug = paginator.page(page)
    except PageNotAnInteger:
        slug = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            return HttpResponse('')
    if request.is_ajax():
        return render(request, 'register/ajax_pag.html', {'slug': slug})
    return render(request, 'register/pagination.html', {'slug': slug})


"""ВЫВОДИТ ГОТОВУЮ ССЫЛКУ НА ЭКРАН И В БД"""


def newgetlink_view(request: HttpRequest) -> HttpResponse:
    lastslug = LinkModel.objects.last()
    return render(request, 'register/nwlnk.html', {'lastslug': lastslug})


""" ПЕРЕВОД НА ИЗНАЧАЛЬНУЮ СТРАНИЦУ ПО НОВОЙ ССЫЛКЕ"""


@login_required(login_url='auth/')
def home_view(request: HttpRequest, link_slug: str) -> HttpResponse:
    home = LinkModel.objects.filter(slug=link_slug)[0]
    if request.method == 'GET':
        LinkModel.objects.filter(slug=link_slug).update(counter=F('counter') + 1)
        return redirect(home.link)
    else:
        raise AssertionError


"""УДАЛЕНИЕ ЗАПИСИ"""


class DelView(DeleteView):
    model = LinkModel
    success_url = reverse_lazy(pagination_view)
    template_name = 'register/delete.html'
