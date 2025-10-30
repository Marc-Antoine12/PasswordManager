from django import forms
from .models import Password


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(required=True)

    def save_user(self):
        from django.contrib.auth.models import User
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email']
        )
        return user
    

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)


class PasswordForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, help_text="The actual password")
    
    class Meta:
        model = Password
        fields = ['title', 'username', 'password', 'url', 'notes', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Gmail, Facebook'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your username/email'}),
            'url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://example.com'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Additional notes'}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Social Media, Work, Banking'}),
        }
    
    def save(self, commit=True):
        instance: Password = super().save(commit=False)
        # Encrypt the password before saving
        raw_password = self.cleaned_data['password']
        instance.set_password(raw_password)
        if commit:
            instance.save()
        return instance