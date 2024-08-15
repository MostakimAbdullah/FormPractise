from django import forms
import datetime



BIRTH_YEAR = ['1998','1999','2000','2001','2002','2003','2004','2005','2006','2007']

class Django_Form(forms.Form):
    name=forms.CharField(label="User Name", widget=forms.TextInput(attrs={'placeholder':'Enter User Name', 'required':'False'}))
    email=forms.EmailField(label="Email Address",initial='mostakimabdulla@gmail.com')
    date=forms.DateField(initial=datetime.date.today)
    birth_year=forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR))
    