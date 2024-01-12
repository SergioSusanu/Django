from django import forms

class ReservationForm(forms.Form):
    name = forms.CharField(max_length=50, label='Name of contact')
    guests = forms.IntegerField(min_value=1, max_value=10)
    date = forms.DateTimeField()
    table = forms.IntegerField()
    celebration = (('1','anniversary'), ('2','birthday'), ('3','other'))
    ocassion = forms.ChoiceField(choices=celebration)
    email = forms.EmailField()
