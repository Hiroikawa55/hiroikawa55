from django.shortcuts import render
# import logging
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import BoardModel
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .forms import FindForm, NearForm, OthersForm
from django.core.paginator import Paginator


def signupfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        try:
            User.objects.get(username=username2)
            return render(request, 'signup.html', {'error':'このユーザーは登録されています'})
        except:
            user = User.objects.create_user(username2, '', password2)
        return render(request, 'signup.html', {'some':100})
    return render(request, 'signup.html', {'some':100})

def loginfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        user = authenticate(request, username=username2, password=password2)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return redirect('login')
    return render(request, 'login.html')

@login_required
def listfunc(request, num=1):
    object_list = BoardModel.objects.order_by("-id")
    page = Paginator(object_list, 50):wq
    return render(request, 'list.html', {'object_list': page.get_page(num)})

# class Listview(LoginRequiredMixin, ListView):
#     model = BoardModel
#     template_name = 'list.html'
#     paginate_by = 2
#
#     def get_queryset(self):
#         object_list = BoardModel.objects.filter(user=self.request.user).order_by('name')
#         return object_list

def logoutfunc(request):
    logout(request)
    return redirect('login')

def detailfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'object':object})

def goodfunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    post.good = post.good +1
    post.save()
    return redirect('list')

def readfunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    post2 = request.user.get_username()
    if post2 in post.readtext:
        return redirect('list')
    else:
        post.read += 1
        post.readtext = post.readtext + ' ' + post2
        post.save()
        return redirect('list')

class BoardEdit(UpdateView):
    template_name = 'edit.html'
    model = BoardModel
    fields = ('name','structure','age', 'age2', 'pref','town','address','roof','memo','others')
    success_url = reverse_lazy('list')

def find(request, form=0, num=1):
    if (request.method == 'POST'):
        msg = '検索結果:'
        form = FindForm(request.POST)
        if form.is_valid():
            c_form = form.cleaned_data['find']
            str = request.POST['find']
            object_list = BoardModel.objects.filter(memo__contains=str)
            page = Paginator(object_list, 100)
    else:
        msg = '検索結果...'
        form = FindForm()
        c_form = FindForm()
        object_list = BoardModel.objects.all()
        page = Paginator(object_list, 100)
    params = {
        'titile': '登録データベース',
        'object_list': page.get_page(num),
        'message': msg,
        'form':form,
        'c_form':c_form
    }
    return render(request, 'find.html', params)

def others(request, c_form=0, num=1):
    if (request.method == 'POST'):
        msg = '検索結果:'
        form = OthersForm(request.POST)
        if form.is_valid():
            c_form = form.cleaned_data['others']
        str = request.POST['others']
        object_list = BoardModel.objects.filter(others__contains=str)
        page = Paginator(object_list, 20)
    else:
        msg = '検索結果...'
        form = OthersForm()
        c_form = OthersForm()
        object_list = BoardModel.objects.all()
        page = Paginator(object_list, 20)
    params = {
        'titile': '登録データベース',
        'object_list': page.get_page(num),
        'message': msg,
        'form':form,
        'c_form':c_form
    }
    return render(request, 'others.html', params)

# class BoardCreate(CreateView):
#     template_name = 'create.html'
#     model = BoardModel
#     fields = ('name', 'memo', 'others')
#     success_url = reverse_lazy('list')

def near(request, form2='aaaa', num=1):
    if (request.method == 'POST'):
        msg = '検索結果'
        form2 = NearForm(request.POST)
        if form2.is_valid():
            c_form = form2.cleaned_data['near']
        str = request.POST['near']
        #object_list = BoardModel.objects.get_queryset().order_by('id')
        #object_list = BoardModel.objects.filter(structure__contains=str)
        #object_list = BoardModel.objects.get_queryset()
        object_list = BoardModel.objects.all()
        page = Paginator(object_list, 20)
    else:
        msg = '検索結果...'
        form2 = NearForm()
        c_form = NearForm()
        object_list = BoardModel.objects.all()
        page = Paginator(object_list, 20)

    params = {
        'titile': '登録データベース',
        'object_list': page.get_page(num),
        'message': msg,
        'form2':form2,
        'c_form':c_form
    }
    return render(request, 'near.html', params)

# class BoardCreate(CreateView):
#     template_name = 'create.html'
#     model = BoardModel
#     fields = ('name', 'memo', 'others')
#     success_url = reverse_lazy('list')

    # def get_context_data(self, **kwargs):
    #     form2 = super(BoardCreate, self).get_context_data(**kwargs)
    #     form2 = BoardModel.objects.all()
    #     # if form2['memo'].is_valid():
    #     # c_form = form2.cleaned_data['memo']
    #     # str = request.POST['near']
    #     #object_list = BoardModel.objects.get_queryset().order_by('id')
    #     #object_list = BoardModel.objects.filter(structure__contains=str)
    #     #object_list = BoardModel.objects.get_queryset()
    #     object_list = BoardModel.objects.all()
    #
    #     params = {
    #         'titile': '重文データベース',
    #         'object_list': object_list,
    #         'form2':form2
    #     }
    #     return render(form2, 'create.html', params)