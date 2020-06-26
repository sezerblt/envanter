from django.shortcuts import render,HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm,ProfileUpdateForm,UserUpdateForm
from django.contrib.auth.decorators import login_required

#kayıt için post metodu kullanim
def register(request):
    #metodumuz POST ise
    if request.method == 'POST':
        #Form objesi olustur
        form = UserRegisterForm(request.POST)
        #orm gcerli ise
        if form.is_valid():
            #formu kaydet button degeri default dur
            form.save()
            #form icerigini temizle
            username = form.cleaned_data.get('username')
            #basarili(yesik fon) mesajı goster
            messages.success(request, f'Hesap {username}! olusturuldu')
            #anassayfaya dön
            return redirect('home_url_name')
    else:
        #varsayılan form objesi
        form = UserRegisterForm()
    #metodu template icerisine render et
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Uyelik Guncellendi!')
            return redirect('profile_url_name')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'users/profile.html', context)
