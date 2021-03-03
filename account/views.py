from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
#from django.http import HttpResponse
#from django.contrib.auth import authenticate, login
from .forms import UserEditForm, MemberEditForm
from django.contrib.auth.models import User
from django.contrib import messages, auth
from .models import Company, Member


"""
# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated '\
                                        'successfully')
                else:
                    return  HttpResponse('Disabled account')

            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return  render(request, 'account/login.html', {'form': form})
"""


@login_required
def dashboard(request):
    member = Member.objects.get(user=request.user)
    show_dash = False
    if member.is_super:
        show_dash = True
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard',
                   'member': member,
                   'show_dash': show_dash})


def register(request):
    if request.method == 'POST':
        company = request.POST['company_name']
        line_of_business = request.POST['line_of_business']
        organisation_type = request.POST['organisation_type']
        organisation_description = request.POST['organisation_description']
        business_registration_number = request.POST['business_registration_number']
        email = request.POST['email']
        contact_number = request.POST['contact_number']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']

        # Check username
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:
                    # Looks good
                    user = User.objects.create_user(username=username, password=password, email='email',
                                                    first_name=first_name, last_name=last_name)

                    # Login after register
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('index')
                    user.save()
                    company = Company.objects.create(name=company, line_of_business=line_of_business, organisation_description=organisation_description,
                                                     organisation_type=organisation_type, business_registration_number=business_registration_number, email=email, contact_number=contact_number)
                    company.save()
                    member = Member.objects.create(user=user, is_super=True, unique_number='000000', country='South Africa')
                    member.save()
                    messages.success(request, 'You are now registered and can log in to continue')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

    return render(request, 'account/register.html')


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        member_form = MemberEditForm(instance=request.user.member,
                                     data=request.POST,
                                     files=request.FILES)
        if user_form.is_valid() and member_form.is_valid():
            user_form.save()
            member_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        member_form = MemberEditForm(instance=request.user.member)
    return render(request,
                  'account/edit.html',
                  {'user_form': user_form,
                   'member_form': member_form})
















