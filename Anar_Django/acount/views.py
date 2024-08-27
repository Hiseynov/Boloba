#views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.utils.encoding import force_str, force_bytes
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from Anar_Django.settings import EMAIL_HOST_USER   
from django.contrib.auth.views import (
                                       PasswordResetView,
                                       PasswordResetConfirmView,
                                       LoginView) 
from .tokens import account_activation_token
from .forms import UserRegisterForm, LoginForm, CustomPasswordResetForm, CustomSetPasswordForm
from .models import User

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    authentication_form = LoginForm
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super(CustomLoginView, self).dispatch(request, *args, **kwargs)

class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'email/password_message.html'
    form_class = CustomPasswordResetForm
    template_name = 'password/password_reset.html'
    success_url = reverse_lazy('login')
    
    def get_success_url(self):
        messages.success(self.request, 'Your request to change your password has been registered. Please check your email.')
        return super(CustomPasswordResetView, self).get_success_url()
    
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password/password_reset_confirm.html'
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy('login')

    def get_success_url(self):
        messages.success(self.request, 'Your password has been successfully changed!')
        return super(CustomPasswordResetConfirmView, self).get_success_url()




from django.contrib.auth.decorators import login_required

@login_required
def myaccount(request):
    user = request.user  # Get the currently logged-in user
    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
    }
    return render(request, 'my-account.html', context)

class RegisterView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super(RegisterView, self).dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
    
        subject = 'Activate Your Account'
        current_site = get_current_site(self.request)
        message = render_to_string('email/confirmation_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
    
        from_email = EMAIL_HOST_USER
        to_email = form.cleaned_data.get('email')
        send_mail(subject, message, from_email, [to_email])
    
        messages.success(self.request, 'Please confirm your email to complete registration.')
        return redirect('login')

    
def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid, is_active=False)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Your profile is activated.')
        return redirect('login')
    else:
        messages.error(request, 'Activation link is invalid!')
        return redirect('/')
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
