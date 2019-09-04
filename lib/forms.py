from django import forms
from.models import Book
from django.contrib.auth.forms import AuthenticationForm

class CreateForm(forms.Form):
    day = forms.DateField()
    book_name = forms.CharField(label='BookName')
    book_category = forms.CharField(label='Category')
    book_author = forms.CharField(label='Author')
    book_context = forms.CharField(label='context')


class createForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['day','book_name','book_category','book_author', 'book_context']
        widgets = {
            'day': forms.SelectDateWidget

        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['day'].widget.attrs.update({'rows' : '3000'})

class FindForm(forms.Form):
    find = forms.CharField(label='Find', required=False)

class EditForm(forms.Form):
    day = forms.DateField()
    book_name = forms.CharField(label='BookName')
    book_category = forms.CharField(label='Category')
    book_author = forms.CharField(label='Author')
    book_context = forms.CharField(label='context')

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        field.widget.attrs['class'] = 'form-control'
        field.widget.attrs['placeholder'] = field.label
