from django.contrib.admin.sites import AdminSite
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.admin.forms import AdminAuthenticationForm
from django.forms import forms
from captcha.fields import ReCaptchaField

class AdminLoginRecaptchaForm(AuthenticationForm):
    recaptcha_token = forms.CharField(required=True)
    captcha = ReCaptchaField()
    class Meta: 
        fields = ['password', 'username',  'captcha']

    def clean(self):
        super().clean()
        
        url = 'https://www.google.com/recaptcha/api/siteverify'
        params = {
            'secret': 'SECRET',
            'response': self.cleaned_data['recaptcha_token']
        }
        
        response = requests.post(url, params)
        if response.status_code == requests.codes.ok:
            print(response.json()['success'])
            print(response.json()['action'])
            if response.json()['success'] and response.json()['action'] == '/admin/login/':
                print('Captcha valid for user={}'.format(self.cleaned_data.get('username')))
            else:
                print('Captcha valid for user={}'.format(self.cleaned_data.get('username')))
                raise forms.ValidationError('ReCAPTCHA is invalid.')
        else:
                print('Captcha valid for user={}'.format(self.cleaned_data.get('username')))
        
        print(self.cleaned_data)
        return self.cleaned_data

AdminSite.login_form = AdminLoginRecaptchaForm