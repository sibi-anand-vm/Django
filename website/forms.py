from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.Models import User
class SignUpForm(UserCreationForm):
	email=forms.CharField(label='Email',widget=Forms.TextInput(attrs={'class':'form-control','placeholder':'Enter email here'})
	first_name=forms.CharField(label='First_name',max_length='25',widget=Forms.TextInput(attrs={'class':'form-control','placeholder':'Enter firstname here'})
	last_name=forms.CharField(label='Last_name',max_length='25',widget=Forms.TextInput(attrs={'class':'form-control','placeholder':'Enter lastname here'})


