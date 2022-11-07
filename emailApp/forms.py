from django import forms 


# email form 
class EmailForm(forms.Form):
    Email = forms.EmailField(required=True, label="Email", help_text="Enter Email to verify")