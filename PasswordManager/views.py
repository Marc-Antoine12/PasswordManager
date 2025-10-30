from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse

from . import forms
from .forms import PasswordForm
from .models import Password


def register(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save_user()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('password_list')
    else:
        form = forms.RegistrationForm()
        
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = forms.LoginForm()
            
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('user_login')

@login_required
def home(request):
    recent_passwords = Password.objects.filter(user=request.user).order_by('-created_at')[:5]
    total_passwords = Password.objects.filter(user=request.user).count()
    context = {
        'recent_passwords': recent_passwords,
        'total_passwords': total_passwords,
    }
    return render(request, 'home.html', context)

@login_required
def password_list(request):
    search_query = request.GET.get('search', '')
    category_filter = request.GET.get('category', '')
    
    passwords = Password.objects.filter(user=request.user)
    
    if search_query:
        passwords = passwords.filter(title__icontains=search_query)
    
    if category_filter:
        passwords = passwords.filter(category=category_filter)
    
    passwords = passwords.order_by('-created_at')
    
    categories = Password.objects.filter(user=request.user).values_list('category', flat=True).distinct()
    
    context = {
        'passwords': passwords,
        'search_query': search_query,
        'category_filter': category_filter,
        'categories': categories,
    }
    return render(request, 'password_list.html', context)

@login_required
def add_new_password(request):
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            new_password = form.save(commit=False)
            new_password.user = request.user
            new_password.save()
            messages.success(request, 'Password added successfully!')
            return redirect('password_list')
    else:
        form = PasswordForm()
    return render(request, 'add_password.html', {'form': form})

@login_required
def edit_password(request, password_id):
    password = get_object_or_404(Password, id=password_id, user=request.user)
    
    if request.method == 'POST':
        form = PasswordForm(request.POST, instance=password)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password updated successfully!')
            return redirect('password_list')
    else:
        form = PasswordForm(instance=password)
    
    return render(request, 'edit_password.html', {'form': form, 'password': password})

@login_required
def delete_password(request, password_id):
    password = get_object_or_404(Password, id=password_id, user=request.user)
    
    if request.method == 'POST':
        password.delete()
        messages.success(request, 'Password deleted successfully!')
        return redirect('password_list')
    
    return render(request, 'confirm_delete.html', {'password': password})