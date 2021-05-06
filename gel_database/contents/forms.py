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

class SelectGene(forms.Form):
	Controlgene = forms.ChoiceField(label="Gene",
		choices=(
			('ACTB.1','ACTB.1'),
			('ACTB.2','ACTB.2'),
			('ACTB.3','ACTB.3'),
			('ACTB','ACTB'),
			('CTCF','CTCF'),
			('EP300','EP300'),
			('SMAD1','SMAD1')
		),
		widget = forms.widgets.RadioSelect())
	Selfrenewalgene = forms.ChoiceField(label="Gene",
		choices=(
			('CXCL5','CXCL5'),
			('DNMT3B','DNMT3B'),
			('HESX1','HESX1'),
			('IDO1','IDO1'),
			('LCK','LCK'),
			('NANOG','NANOG'),
			('POU5F1','POU5F1'),
			('SOX2','SOX2'),
			('TRIM22','TRIM22')
		),
		widget = forms.widgets.RadioSelect())
	Ectodermgene = forms.ChoiceField(label="Gene",
		choices=(
			('CDH9','CDH9'),
			('COL2A1','COL2A1'),
			('DMBX1','DMBX1'),
			('DRD4','DRD4'),
			('EN1','EN1'),
			('LMX1A','LMX1A'),
			('MAP2','MAP2'),
			('MYO3B','MYO3B'),
			('NOS2','NOS2'),
			('NR2F1-NR2F2','NR2F1-NR2F2'),
			('NR2F2','NR2F2'),
			('OLFM3','OLFM3'),
			('PAPLN','PAPLN'),
			('PAX3','PAX3'),
			('PAX6','PAX6'),
			('POU4F1','POU4F1'),
			('PRKCA','PRKCA'),
			('SDC2','SDC2'),
			('SOC1','SOX1'),
			('TRPM8','TRPM8'),
			('WNT1','WNT1'),
			('ZBTB16','ZBTB16')
		),
		widget = forms.widgets.RadioSelect())
	Endodermgene = forms.ChoiceField(label="Gene",
		choices=(
			('AFP','AFP'),
			('CABP7','CABP7'),
			('CDH20','CDH20'),
			('CLDN1','CLDN1'),
			('CPLX2','CPLX2'),
			('ELAVL3','ELAVL3'),
			('EOMES','EOMES'),
			('FOXA1','FOXA1'),
			('FOXA2','FOXA2'),
			('FOXP2','FOXP2'),
			('GATA4','GATA4'),
			('GATA6','GATA6'),
			('HHEX','HHEX'),
			('HMP19','HMP19'),
			('HNF1B','HNF1B'),
			('HNF4A','HNF4A'),
			('KLF5','KLF5'),
			('LEFTY1','LEFTY1'),
			('LEFTY2','LEFTY2'),
			('NODAL','NODAL'),
			('PHOX2B','PHOX2B'),
			('POU3F3','POU3F3'),
			('PRDM1','PRDM1'),
			('RXRG','RXRG'),
			('SOX17','SOX17'),
			('SST','SST')
		),
		widget = forms.widgets.RadioSelect())
	Mesodermgene = forms.ChoiceField(label="Gene",
		choices=(
			('ABCA4','ABCA4'),
			('ALOX15','ALOX15'),
			('BMP10','BMP10'),
			('CDH5','CDH5'),
			('CDX2','CDX2'),
			('COLEC10','COLEC10'),
			('ESM1','ESM1'),
			('FCN3','FCN3'),
			('FOXF1','FOXF1'),
			('HAND1','HAND1'),
			('HAND2','HAND2'),
			('HEY1','HEY1'),
			('HOPX','HOPX'),
			('IL6ST','IL6ST'),
			('NKX2-5','NKX2-5'),
			('ODAM','ODAM'),
			('PDGFRA','PDGFRA'),
			('PLVAP','PLVAP'),
			('RGS4','RGS4'),
			('SNAI2','SNAI2'),
			('TBX3','TBX3'),
			('TM4SF1','TM4SF1')
		),
		widget = forms.widgets.RadioSelect())
	Mesendodermgene = forms.ChoiceField(label="Gene",
		choices=(
			('FGF4','FGF4'),
			('GDF3','GDF3'),
			('NPPB','NPPB'),
			('NR5A2','NR5A2'),
			('PTHLH','PTHLH'),
			('T','T')
		),
		widget = forms.widgets.RadioSelect())
	Othergene = forms.ChoiceField(label="Gene",
		choices=(
			('CD44','CD44'),
			('JARID2','JARID2'),
			('MYC','MYC'),
			('SEV','SEV')
		),
		widget = forms.widgets.RadioSelect())

class SelectSimPic(forms.Form):
	simparameter = forms.ChoiceField(label="simparameter: ",
		choices=(
			('parameter','parameter'),
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

class UploadExpData(forms.Form):
	Datatypes = forms.ChoiceField(label="types",
		choices=(
			('mechanical','mechanical'),
			('score','score'),
			('CtValue','Ct values'),
			('FoldChange','Fold changes')
		))


