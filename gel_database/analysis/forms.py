from django import forms

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
			('CDH9','CDH9 (鈣粘蛋白)'),
			('COL2A1','COL2A1 (軟骨、骨骼)'),
			('DMBX1','DMBX1 (神經脊)'),
			('DRD4','DRD4 (神經元)'),
			('EN1','EN1 (中樞神經)'),
			('LMX1A','LMX1A (神經元)'),
			('MAP2','MAP2 (神經元)'),
			('MYO3B','MYO3B (耳蝸)'),
			('NOS2','NOS2 (神經)'),
			('NR2F1-NR2F2','NR2F1-NR2F2 (視黃酸)'),
			('NR2F2','NR2F2 (視黃酸)'),
			('OLFM3','OLFM3 (神經視覺)'),
			('PAPLN','PAPLN (角皮層)'),
			('PAX3','PAX3 (神經、肌肉)'),
			('PAX6','PAX6 (眼睛發育)'),
			('POU4F1','POU4F1 (視網膜神經節)'),
			('PRKCA','PRKCA (心肌收縮、神經膠質)'),
			('SDC2','SDC2 (樹突神經)'),
			('SOC1','SOX1 (神經元)'),
			('TRPM8','TRPM8 (感覺神經元)'),
			('WNT1','WNT1 (中樞神經、成骨細胞)'),
			('ZBTB16','ZBTB16 (先天性淋巴細胞分化)')
		),
		widget = forms.widgets.RadioSelect())
	Endodermgene = forms.ChoiceField(label="Gene",
		choices=(
			('AFP','AFP (卵黃囊、肝臟)'),
			('CABP7','CABP7 (視網膜)'),
			('CDH20','CDH20 (鈣粘蛋白)'),
			('CLDN1','CLDN1 (上皮或內皮細胞、膽管)'),
			('CPLX2','CPLX2 (調節囊泡)'),
			('ELAVL3','ELAVL3 (腦脊髓、感覺神經)'),
			('EOMES','EOMES (中樞神經、胃形成)'),
			('FOXA1','FOXA1 (肝)'),
			('FOXA2','FOXA2 (肝)'),
			('FOXP2','FOXP2 (大腦、肺、腸)'),
			('GATA4','GATA4 (心肌分化、睾丸發育)'),
			('GATA6','GATA6 (腸、肺、心臟)'),
			('HHEX','HHEX (造血分化)'),
			('HMP19','HMP19 (神經泡囊)'),
			('HNF1B','HNF1B (胰腺)'),
			('HNF4A','HNF4A (肝、腎、腸)'),
			('KLF5','KLF5 (促進和抑制細胞增殖、心血管)'),
			('LEFTY1','LEFTY1 (確定器官系統左右不對稱、心血管筋膜)'),
			('LEFTY2','LEFTY2 (確定器官系統左右不對稱、子宮內膜出血)'),
			('NODAL','NODAL (內臟異位)'),
			('PHOX2B','PHOX2B (神經遞質)'),
			('POU3F3','POU3F3 (神經系統)'),
			('PRDM1','PRDM1 (淋巴)'),
			('RXRG','RXRG (肺)'),
			('SOX17','SOX17 (膀胱輸尿管、腸)'),
			('SST','SST (胃、腸道)')
		),
		widget = forms.widgets.RadioSelect())
	Mesodermgene = forms.ChoiceField(label="Gene",
		choices=(
			('ABCA4','ABCA4 (視網膜)'),
			('ALOX15','ALOX15 (角膜、巨噬細胞、骨骼、脂肪細胞、胰島、肝臟)'),
			('BMP10','BMP10 (心血管、肌細胞增殖、心臟大小的調節)'),
			('CDH5','CDH5 (血管管腔)'),
			('CDX2','CDX2 (小腸和大腸的腸上皮內層)'),
			('COLEC10','COLEC10 (細胞遷移的調控)'),
			('ESM1','ESM1 (肺和腎的內皮、血管生成)'),
			('FCN3','FCN3 (肺泡中、肝臟)'),
			('FOXF1','FOXF1 (肺泡毛細血管發育)'),
			('HAND1','HAND1 (心臟發育)'),
			('HAND2','HAND2 (心臟發育)'),
			('HEY1','HEY1 (心臟瓣膜、心臟隔膜、神經元前體細胞)'),
			('HOPX','HOPX (心臟發育)'),
			('IL6ST','IL6ST (感覺神經元、星形膠質細胞、成骨細胞)'),
			('NKX2-5','NKX2-5 (心臟發育、脾臟發育)'),
			('ODAM','ODAM (牙齒生成)'),
			('PDGFRA','PDGFRA (骨骼發育、頭顱閉合)'),
			('PLVAP','PLVAP (內皮)'),
			('RGS4','RGS4 (G蛋白)'),
			('SNAI2','SNAI2 (神經脊、成骨細胞)'),
			('TBX3','TBX3 (四肢、牙齒、頭髮、生殖器)'),
			('TM4SF1','TM4SF1 (細胞表面蛋白)')
		),
		widget = forms.widgets.RadioSelect())
	Mesendodermgene = forms.ChoiceField(label="Gene",
		choices=(
			('FGF4','FGF4 (正常四肢、心臟瓣膜發育)'),
			('GDF3','GDF3 (眼睛和骨骼發育)'),
			('NPPB','NPPB (心血管)'),
			('NR5A2','NR5A2 (膽汁酸合成、肝、胰腺)'),
			('PTHLH','PTHLH (乳腺和牙齒形成)'),
			('T','T (骨、心臟)')
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


