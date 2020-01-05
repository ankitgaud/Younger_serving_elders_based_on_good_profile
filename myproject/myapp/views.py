from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from .forms import *
from .models import *

# Create your views here.
def home(request):
	return render(request, 'home.html')

@login_required
def number_of_oldies(request, username, username1):
	if request.method == 'post':
		form = younger_table_form(request.POST)
		if form.is_valid():
			data = younger_table.objects.get(elder_user=username1)
			rating1 = form.cleaned_data.get('rating_by_younger')
			review1 = form.cleaned_data.get('review_by_younger')
			data.rating_by_younger = rating1
			data.review_by_younger = review1
			data.save()
		return redirect('younger_self_profile', username)
	else:
		form = younger_table_form()
		return render(request, 'testing.html', {'form': form, 'username':username1})
	

@login_required
def younger_user(request, username):
	try:
		data = Young_user.objects.get(Y_username=username)
		data2 = Current_status_younger.objects.get(username=username)
		data3 = younger_table.objects.filter(younger_user=username)
		context={
		'user_data':data,'user_name':username, 'status':data2, 'oldies':data3
		}
		return render(request, 'young_user.html', context)
	except:
		print('error')

@login_required
def elder_user(request, username):
	try:
		data = ELDER_user.objects.get(E_username=username)
		data2 = elder_table.objects.filter(elder_user=username)
		context ={
		'user_data': data, 'user_name':username, 'younger_':data2
		}
		
		return render(request, 'elder_user.html', context)
	except:
		print('error')



def login_view(request, type1):
	print(type1)
	next = request.GET.get('next')
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		login(request, user)
		if type1 == 'younger':

			if next:
				return redirect(next)
			return redirect('younger_self_profile', username=username)
		else:
			if next:
				return redirect(next)
			return redirect('elder_self_profile', username=username)


	context = {
		'form': form,
	}
	return render(request, "login.html", context)


def register_view(request,type1):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('home')

    context = {
        'form': form,
    }
    return render(request, "signup.html", context)


def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def younger_self_profile(request, username):
	try:
		data = Young_user.objects.get(Y_username=username)
		data2 = Current_status_younger.objects.get(username=username)
		data3 = younger_table.objects.filter(younger_user=username)
		context={
		'user_data':data,'user_name':username, 'status':data2, 'oldies':data3
		}
		return render(request, 'young_user_self.html', context)
	except:
		try:
			data = ELDER_user.objects.get(E_username=username)
			context ={
			'user_data': data, 'user_name':username
			}
			return redirect('elder_self_profile', username=username)
		except:
			return redirect('younger_edit_profile', username=username)


@login_required
def elder_self_profile(request, username):
	try:
		data = ELDER_user.objects.get(E_username=username)
		data2 = elder_table.objects.filter(elder_user=username)
		#data3 = 
		context ={
		'user_data': data, 'user_name':username, 'younger_':data2
		}
		
		return render(request, 'elder_user_self.html', context)
	except:
		try:
			data = Young_user.objects.get(Y_username=username)

			context={
			'user_data':data,'user_name':username
			}
			return redirect('younger_self_profile', username=username)
		except:
			return redirect('elder_edit_profile', username=username)


@login_required
def younger_edit_profile(request, username):
	if request.method == "POST":
		form = younger_user_form(request.POST)
		if form.is_valid():
			form.save()
		data2 = Current_status_younger(username=username)
		data2.save()
		return redirect('younger_user', username=username)
	else:
		form = younger_user_form()
		return render(request, 'edit_younger_profile.html', {'form': form, 'user_name':username})


@login_required
def elder_edit_profile(request, username):
	if request.method == "POST":
		form = elder_user_form(request.POST)
		if form.is_valid():
			form.save()
		return redirect('elder_user', username=username)
	else:
		form = elder_user_form()
		return render(request, 'edit_elder_profile.html', {'form': form, 'user_name': username})


#@login_required
def edit_current_status(request, username):
	data2 = Current_status_younger.objects.get(username=username)

	if request.method == "POST":
		elder1 = request.POST.get('elder_1')
		elder2 = request.POST.get('elder_2')
		elder3 = request.POST.get('elder_3')
		elder4 = request.POST.get('elder_4')
		elder6 = request.POST.get('elder_6')

		try:
			if elder1 != '' and ELDER_user.objects.get(E_username=elder1) != '':
				data2.elder_1 = elder1

			if elder2 != '' and ELDER_user.objects.get(E_username=elder2) != '':	
				data2.elder_2 = elder2
		
			if elder2 != '' and ELDER_user.objects.get(E_username=elder3) != '':
				data2.elder_3 = elder3
		
			if elder2 != '' and ELDER_user.objects.get(E_username=elder4) != '':
				data2.elder_4 = elder4
			
			if elder2 != '' and ELDER_user.objects.get(E_username=elder6) != '':
				data2.elder_6 = elder6
			data2.save()
		except:
			error = "You had entered invalid elder username"
			return render(request, 'current_status.html', {'status':data2, 'username':username, 'error': error})

		
		return redirect('younger_self_profile', username)
	return render(request, 'current_status.html', {'status':data2, 'username':username})


def remove_user_from_current_status(request, username, username1):
	data2 = Current_status_younger.objects.get(username=username)
	if username1 == 'elder_1':
		data2.elder_1 = ''
	if username1 == 'elder_2':
		data2.elder_2 = ''
	if username1 == 'elder_3':
		data2.elder_3 = ''
	if username1 == 'elder_4':
		data2.elder_4 = ''
	if username1 == 'elder_6':
		data2.elder_6 = ''	

	data2.save()
	
	return redirect('younger_self_profile', username)


def add_elders_in_your_list(request, username):
	form = add_elders_in_list(request.POST)
	form1 = add_elders_in_list()
	if form.is_valid():
		try:
			abc = form.cleaned_data.get('elder_user')
			if ELDER_user.objects.get(E_username=abc) != '':
				user = form.save(commit=False)
				user.younger_user = username
				form.save()
			return redirect('younger_self_profile', username)
		except:	
			error = "You had entered invalid elder username"
			return render(request, 'add_elder.html', {'form': form1, 'username':username, 'error': error})
	return render(request, 'add_elder.html', {'form': form1, 'username':username})

def Add_younger_in_elder_table(request, username):
	form = add_younger_in_elder_table(request.POST)
	form1 = add_younger_in_elder_table()
	if form.is_valid():
		try:
			abc = form.cleaned_data.get('younger_user')
			if Young_user.objects.get(Y_username=abc) != '':
				user = form.save(commit=False)
				user.elder_user = username
				form.save()
			return redirect('elder_self_profile', username)
		except:
			error = "You had entered invalid younger username"
			return render(request, 'add_younger.html', {'form': form1, 'username': username, 'error': error})
	return render(request, 'add_younger.html', {'form': form1, 'username': username})



