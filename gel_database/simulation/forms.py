from django import forms


class SelectSimPic(forms.Form):
	simparameter = forms.ChoiceField(label="simparameter: ",
		choices=(
			('parameter','parameter'),
		),
		required = False,
		widget = forms.widgets.RadioSelect())
	dynamicmech = forms.ChoiceField(label="Scope: ",
		choices=(
			('macro','macroscope'),
			('micro','microscope')
		),
		required = False,
		widget = forms.widgets.RadioSelect())
	simpicture = forms.ChoiceField(label="simpicture: ",
		choices=(
			('result picture','picture'),
		),
		required = False,
		widget = forms.widgets.RadioSelect())
	gelma = forms.ChoiceField(label="Gelma concentration: ",
		choices=(
			('-','-'),
			(0.1,0.1),
			(0.125,0.125),
			(0.15,0.15),
			(0.175,0.175)
		))
	cure = forms.ChoiceField(label="Cure adhesive types: ",
		choices=(
			('-','-'),
			('LAP','LAP')
		))
	adhesive = forms.ChoiceField(label="Adhesive concentration: ",
		choices=(
			('-','-'),
			(0.0025,0.0025),
			(0.005,0.005)
		))
	light = forms.ChoiceField(label="Light cure time: ",
		choices=(
			('-','-'),
			(30,30),
			(50,50),
			(70,70),
			(90,90)
		))
	groove = forms.ChoiceField(label="Groove angle: ",
		choices=(
			('-','-'),
			(0,0),
			(5,5),
			(10,10),
			(15,15),
			(20,20),
			(25,25),
			(30,30),
			(35,35),
			(40,40),
			(50,50),
			(55,55),
			(60,60),
			(65,65),
			(70,70),
			(75,75),
			(80,80),
			(85,85),
			(90,90)
		))

