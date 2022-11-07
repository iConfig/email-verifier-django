from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from . forms import EmailForm
from django.contrib import messages
import requests
# Create your views here.




def emailcheck(request):
    apikey = "c1c83103-f351-4fae-b924-6a101957040e"
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['Email']
            email_address = email
            response = requests.get(
            "https://isitarealemail.com/api/email/validate",
            params = {'email': email_address},
            headers = {'Authorization': "Bearer " + apikey })

            status = response.json()['status']
            if status == 'valid':
                result = "email is valid"
                messages.success(request, f"{result}")
            elif status == 'invalid':
                result = "email is not valid"
                messages.error(request, f"{result}")
            else:
                result = "email status is unknown"
                messages.info(request, f"{result}")
            return redirect('email_check')
        else:
            messages.error(request, "email is not valid")
        return redirect('email_check')
    else:
        form = EmailForm()
    return render(request, 'home.html', {'form':form})
 

