from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import File
class SignUpForm(UserCreationForm):
	email=forms.EmailField(label='Email',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter email here'}))
	first_name=forms.CharField(label='First_name',max_length='25',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter firstname here'}))
	last_name=forms.CharField(label='Last_name',max_length='25',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter lastname here'}))


	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	
class Addfile(forms.ModelForm):
	first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Firstname'}))     
	last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Lastname'}))
	email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter email'}))
	address=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter address'}))
	state=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter state'}))
	pincode=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter pincode'}))
	class Meta:
		model=File
		exclude=("username",)