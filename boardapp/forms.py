from django import forms

class FindForm(forms.Form):
    find = forms.CharField(label='Find', required=False)

class NearForm(forms.Form):
    near = forms.CharField(label='Near', required=False)

class OthersForm(forms.Form):
    others = forms.CharField(label='Others', required=False)