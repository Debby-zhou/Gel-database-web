from django import forms
class SelectDataForm(forms.Form):
	time = forms.ChoiceField(label='Time', choices=((0,'2020/03/17'),(1,'2020/10/16'),), widget=forms.widgets.RadioSelect(),error_messages={
            "required": "不能為空"})

	table = forms.ChoiceField(label='Type', choices=((0,'Material parameter'),(1, 'Score'),(2,'CT value'),(3, 'Fold change'),), widget=forms.widgets.RadioSelect())
	print("")

