from django.contrib.auth import authenticate, login


def usual_login_view(request):
    """Регистрация и отправка письма с кодом"""
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        OneTimeCode.objects.create(code=random.choice('asdd'), user=user)
        # send one-time code to email
        # redirect somewere
    else: pass
        #return an 'Invdlid login' error message.


def login_with_code_view(request):
    username = request.POST['username']
    code = request.POST['code']
    if OneTimeCode.objects.filter(code=code, user__username=username).exist():
        login(request, user)
    else: pass #error