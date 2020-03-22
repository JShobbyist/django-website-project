from django import forms

class MySearchForm(forms.Form):
    bba_subscription = forms.BooleanField(required=False)
    bba_perspective = forms.BooleanField(required=False)
    bba_report = forms.BooleanField(required=False)
    bba_article = forms.BooleanField(required=False)
    bba_case_study = forms.BooleanField(required=False)