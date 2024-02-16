from django import forms

from myauth.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "first_name", "last_name", "bio", "agreement_accepted", "avatar"


