from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, logout
from django.http import JsonResponse
from .models import PasswordReset, UserProfile
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content, ReplyTo
from django.contrib import messages
from django.views.static import serve
from django.conf import settings


# Create your views here.
def dashboard(request):
    return render(request, 'login.html')


def login(request):
    if request.method == "POST":
        username = request.POST["email"]
        password = request.POST["password"]
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                auth_login(request, user)
            else:
                messages.error(request, "Invalid Credential.", extra_tags='error')
                # return render(request, 'login.html', {'messages': "Invalid Credential.", 'tag': 'error'})
                return render(request, 'login.html')
        except User.DoesNotExist:
            messages.error(request, "Invalid Credential.", extra_tags='error')
            return render(request, 'login.html')
        
    return redirect("dashboard")


def logout_view(request):
    logout(request)
    return redirect("dashboard")


def profile_view(request):
    if request.method == "POST":
        try:
            name = request.POST["name"]
            file = request.FILES['file']
            user = request.user
            user.username = name
            try:
                profile = UserProfile.objects.get(user=user)
            except:
                profile = UserProfile.objects.create(user=user)
            profile.avatar = file
            media_path = settings.MEDIA_ROOT
            with open(media_path + 'userprofile/' + file.name, 'wb+') as f:
                for chunk in file.chunks():
                    f.write(chunk)
            user.save()
            profile.save()
        except:
            name = request.POST["name"]
            user = request.user
            user.username = name
            user.save()
        return JsonResponse({'status': 'success', 'message': 'data updated'})
    else:
        return render(request, 'profile.html')


def media_files(request, path):
    if request.user.is_authenticated:
        if 'ebook' in path.split('/')[3]:
            if 'epub' in path:
                return serve(request, path.replace('.epub', '.pdf'), document_root=settings.MEDIA_ROOT)
            else:
                return serve(request, path.replace('.mobi', '.pdf'), document_root=settings.MEDIA_ROOT)
        return serve(request, path, document_root=settings.MEDIA_ROOT)
    else:
        return redirect('dashboard')


def forgot_password(request):
    if request.method == "POST":
        email = request.POST["email"]
        try:
            user = User.objects.get(email=email)
            if user:  # and to_emails.is_active:
                passworduid = PasswordReset.objects.create(user=user)
                buildurl = request.build_absolute_uri("/") + "auth/password-reset/" + str(passworduid.code)
                send_email(buildurl, email)
                return JsonResponse(
                    {'success': 'true', 'message': 'We have sent password reset email to your email account.', 'tag': 'success'})
            return JsonResponse({'success': 'true', 'message': 'User does not exist.', 'tag': 'error'})
        except User.DoesNotExist:
            return JsonResponse({'success': 'true', 'message': 'User does not exist.', 'tag': 'error'})
    else:
        return render(request, 'forgot.html')


def password_reset(request, uid):
    if request.method == "POST":
        confirm_password = request.POST["confirm_password"]
        new_password = request.POST["new_password"]
        if new_password == confirm_password:
            u = PasswordReset.objects.get(code=uid)
            user = u.user
            user.set_password(new_password)
            user.save()
            messages.success(request, "Password successfully updated!", extra_tags='success')
            # return render(request, 'login.html', {'messages': "Password successfully updated!.", 'tag': 'success'})
            return render(request, 'login.html')
        else:
            messages.error(request, "Password does not match.")
            return render(request, "reset.html",)
    else:
        return render(request, "reset.html")


def send_email(buildurl, to_email):
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("shivani@creativebuffer.com")
    to_email = To(to_email)
    subject = "Reset your password"
    content = Content("text/plain", "Reset your password by clicking: "+buildurl)
    message = Mail(from_email=from_email, to_emails=to_email,
                   subject=subject,
                html_content=content)

    sg.send(message)

