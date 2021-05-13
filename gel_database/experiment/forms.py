from django import forms

class SelectData(forms.Form):
	mechanical = forms.ChoiceField(label="Mechanical properties",
		choices=(
			('parameter','Material parameter'), #,一定要加
		),
		required = False,
		widget = forms.widgets.RadioSelect())
	cell_diff_expression = forms.ChoiceField(label="Expression data",
		choices=(
			('score','Score'),
			('CtValue','CT values'),
			('FoldChange','Fold changes')
		),
		required = False,
		widget = forms.widgets.RadioSelect())
	cell_diff_tissue = forms.ChoiceField(label="Tissue categories",
		choices=(
			('Control','control'),
			('Ectoderm','ectoderm'),
			('Endoderm','endoderm'),
			('Mesendoderm','mesendoderm'),
			('Mesoderm','mesoderm'),
			('Other','other'),
			('Selfrenewal','selfrenewal')
		),
		required = False,
		widget = forms.widgets.RadioSelect())

class UploadExpData(forms.Form):
	Datatypes = forms.ChoiceField(label="types",
		choices=(
			('mechanical','mechanical'),
			('score','score'),
			('CtValue','Ct values'),
			('FoldChange','Fold changes')
		))
