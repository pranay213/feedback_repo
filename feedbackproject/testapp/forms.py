from django import forms
from django.core import validators

class FeedBackForm(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(label='password(again)',widget=forms.PasswordInput)
    feedback=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])
    bot_handler=forms.CharField(required=False,widget=forms.HiddenInput)

    def clean_name(self):
        inputname=self.cleaned_data['name']
        print('validating name')
        if len(inputname)<4:
            raise forms.ValidationError('The length of name field should be >=4')
        return inputname
    def clean_rollno(self):
        inputrollno=self.cleaned_data['rollno']
        print('validating rollno')



















    def clean(self):
        print('Total Form Validation...')
        cleaned_data=super().clean()
        inputname=cleaned_data['name']
        if len(inputname) < 10:
            raise forms.ValidationError('Name should compulsory contain minimum 10 characters')

        inputpwd=cleaned_data['password']
        inputrpwd=cleaned_data['rpassword']
        if inputpwd != inputrpwd:
            raise forms.ValidationError('passwords are not matched')
        bothandler_value=cleaned_data['bot_handler']
        if len(bothandler_value) > 0:
            raise forms.ValidationErr('Thanks Bot!!!')
