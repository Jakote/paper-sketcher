from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, CS_Research_Paper, CS_Proposal, CS_Thesis, IS_Thesis, IS_Proposal, IS_Research_Paper


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["level_of_knowledge","domain_of_Knowledge","type_of_paper"]

class CSResearchpaperForm(forms.ModelForm):
    class Meta:
        model = CS_Research_Paper
        fields = '__all__'
        exclude = ['author']

class CSProposalForm(forms.ModelForm):
    class Meta:
        model = CS_Proposal
        fields = '__all__'
        exclude = ['author']

class CSThesisForm(forms.ModelForm):
    class Meta:
        model = CS_Thesis
        fields = '__all__'
        exclude = ['author']

class ISThesisForm(forms.ModelForm):
    class Meta:
        model = IS_Thesis
        fields = '__all__'
        exclude = ['author']

class ISProposalForm(forms.ModelForm):
    class Meta:
        model = IS_Proposal
        fields = '__all__'
        exclude = ['author']

class ISResearchpaperForm(forms.ModelForm):
    class Meta:
        model = IS_Research_Paper
        fields = '__all__'
        exclude = ['author']