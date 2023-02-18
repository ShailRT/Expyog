from django.shortcuts import render, redirect
from cms.models import Blog
from .forms import RegistrationForm, EditProfile
from django.contrib.auth import login, logout, authenticate
from .models import Profile, UserDetail
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from discuss.models import Query
from django.template.defaultfilters import slugify
from django.core.paginator import Paginator

def user_profile(request, pk):
    user = User.objects.filter(id=int(pk)).first()
    user_profile = Profile.objects.filter(user=user).first()
    user_status = UserDetail.objects.filter(user=user).first()
    user_status = user_status.approved
    user_speciality = ""
    if user_profile.speciality:
        user_speciality = user_profile.speciality.split(',')
    
    context = {
        'user_profile': user_profile,
        'user_on': user,
        'user_status': user_status,
        'user_speciality': user_speciality,

    }

    return render(request, 'user-details.html', context)

@login_required(login_url='/account/login')
def edit_profile(request):
    user = request.user
    user_profile = Profile.objects.filter(user=user).first()
    if request.method == "POST":
        speciality = request.POST.getlist('speciality')
        special = speciality[0]
        for i in range(1,len(speciality)):
            special = f"{special}, {speciality[i]}"


        form = EditProfile(request.POST, instance=user_profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.speciality = special
            profile.save()
            user_profile = Profile.objects.filter(user=user).first()
            return redirect('edit-profile')
        else:
            print("fail")

    else:
        user_status = UserDetail.objects.filter(user=request.user).first()
        user_status = user_status.approved
        form = EditProfile()
        context =  {
            'user_profile': user_profile,
            'form': form,
            'user': request.user,
            'user_status': user_status,
            
        }
        return render(request, 'user-details-edit.html', context)

@login_required(login_url='/account/login')
def user_question(request):
    user = request.user

    question = Query.objects.filter(assigned_user=None)
    paginator = Paginator(question, 4)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    user_status = UserDetail.objects.filter(user=request.user).first()
    user_status = user_status.approved

    context = {
        'questions': page_obj, 
        'user_on': request.user,
        'user_status': user_status
    }

    return render(request, 'user-question.html', context)

@login_required(login_url='/account/login')
def user_question_list(request):
    user = request.user

    categories = {
    'question-assigned': ['Question Assigned',''],
    'question-asked':['Question Asked',''],
    }

    page = request.GET.get('page')
    ptype = request.GET.get('ptype')

    if ptype == 'question-asked':
        question = Query.objects.filter(user=user)
        categories['question-asked'][1] = 'Active'

    elif ptype == 'question-assigned':
        question = Query.objects.filter(assigned_user=user)
        categories['question-assigned'][1] = 'Active'

    else:
        question = Query.objects.filter(assigned_user=user)
        categories['question-assigned'][1] = 'Active'


    paginator = Paginator(question, 4)
    page_obj = paginator.get_page(page)
        
    user_status = UserDetail.objects.filter(user=request.user).first()
    user_status = user_status.approved

    context = {
        'questions': page_obj,
        'user': user,
        'ptype': ptype,
        'categories': categories,
        'user_status': user_status

    }

    return render(request,'user-question-list.html', context)

def question_assignment(request,pk):
    question = Query.objects.filter(query_id=pk).first()
    question.assigned_user = request.user
    question.save()
    return redirect('user-question')

def index(request):
    user = request.user
    categories = {
    '':['Home',''],
    'income-tax':['Income Tax',''],
    'corporate-mattersllp': ['Corporate Matters/LLP',''],
    'audit-assurance-and-accounting-standards': ['Audit & Assurance and Accounting Standards',''],
    'goods-and-services-tax-gst': ['Goods and Services Tax (GST)',''],
    }

    category = request.GET.get('category')
    current_category = category
    if category=="":
        question = Query.objects.all()
        categories[''][1] = 'active'
    else:
        question = Query.objects.filter(category=category)

        for i in categories.keys():
            if i == category:
                categories[i][1] = 'active'
    
    paginator = Paginator(question, 4)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

              
    context = {
        'user': user,
        'questions': page_obj,
        'categories': categories,
        
        'current_category': current_category,
    }
    return render(request, 'index.html', context)

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about-us.html')

def contact(request):
    return render(request, 'contact-us.html')

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def blog_list(request):
    blog_list = Blog.objects.all()
    context = {
        'blog_list': blog_list,
    }
    return render(request, 'blog-list.html', context)

def question(request):
    return render(request, 'question-details.html')

def sign_up(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            user_detail = UserDetail.objects.create(user=user, type=request.POST['user_type'])
            user_detail.save()

            user_profile = Profile.objects.create(user=user)
            user_profile.save()

            return redirect('/?category=&page=1')
    else:
        form = RegistrationForm()
    
    return render(request, 'registration/sign-up.html', {"form": form} )
