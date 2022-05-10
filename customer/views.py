from django.shortcuts import render
from boram3.models import Signup

def customer(request):
    if (request.session.get('username')):
        user_id = request.session.get('username')
        user = Signup.objects.get(userid=user_id)
        return render(request, 'customer.html',{'userinfo': user})
    else:
        return render(request, 'customer.html')


