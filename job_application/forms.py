from django import forms


class ApplicationForm(forms.Form):
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    date = forms.DateField()
    city = forms.CharField(max_length=80)
    occupation = forms.CharField(max_length=80)


class UserMessageForm(forms.Form):
    user_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    subject = forms.CharField(max_length=250)
    message = forms.CharField(max_length=500)
