from django.contrib.auth.forms import AuthenticationForm

class FormLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['Placeholder']='user name (e.g. Lucas)'
        self.fields['password'].widget.attrs['class']='form-control'
        self.fields['password'].widget.attrs['placeholder']='password'