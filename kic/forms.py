from django import forms


class ContactusForm(forms.Form):
    full_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Full name'})
    )
    email = forms.EmailField(
        max_length=255, widget=forms.EmailInput(attrs={'placeholder': 'Email address'})
    )
    phone_number = forms.CharField(
        max_length=10, widget=forms.TextInput(attrs={'placeholder': 'Phone number'})
    )
    subject = forms.CharField(
        max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Subject'})
    )
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(attrs={'placeholder': 'Enter your message', 'rows': 3}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
