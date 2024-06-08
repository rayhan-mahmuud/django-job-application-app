from django.shortcuts import render
from . forms import ApplicationForm, UserMessageForm
from . models import JobForm, UserMessage
from django.contrib import messages


def index(request):

    if request.method == 'POST':
        form = ApplicationForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            city = form.cleaned_data["city"]
            occupation = form.cleaned_data["occupation"]

            JobForm.objects.create(first_name=first_name, last_name=last_name, email=email,
                                   date=date, city=city, occupation=occupation)
            messages.success(request, "Application Submitted Successfully!")

    return render(request, "index.html")


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        form = UserMessageForm(request.POST)

        if form.is_valid():
            user_name = form.cleaned_data["user_name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]

            UserMessage.objects.create(user_name=user_name, email=email, subject=subject, message=message)

            messages.success(request,"We have received your message and will get back to you ASAP. Thanks!")

    return render(request, 'contact us.html')
