from django.contrib import admin
from . import models

# Register your models here.
# 每個table一定要有PRIMARY KEY
admin.site.register(models.E200317Score)
admin.site.register(models.E200317CtValues)
admin.site.register(models.E200317FoldChange)
admin.site.register(models.E200317Parameter)
admin.site.register(models.E201016Parameter)
admin.site.register(models.E201016Score)

