
from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'имя' }),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'phone'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'message', 'rows': 5}),
        }

    # name = forms.CharField(max_length=30, leble='Имя', help_text="qweretrewwqer",
    #                        widget=forms.TextInput(
    #                            attrs={"class": "form_control", "placeholder": "Имя"}
    #                        ))
    # email = forms.EmailField(leble='почта', help_text="qweretrewwqer почта",
    #                        widget=forms.EmailInput(
    #                            attrs={"class": "form_control", "placeholder": "почта"}
    #                        ))
    # phone = forms.CharField(max_length=30, leble='телефон', help_text="qweretrewwqer номер",
    #                        widget=forms.TextInput(
    #                            attrs={"class": "form_control", "placeholder": "номер"}
    #                        ))
    # message = forms.CharField(max_length=300, leble='сообщения', help_text="qweretrewwqer сообщения",
    #                        widget=forms.Textarea(
    #                            attrs={"class": "form_control", "placeholder": "сообщения",
    #                                   'row': 5}
    #                        ))





