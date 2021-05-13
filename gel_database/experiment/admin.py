from django.contrib import admin
from .models import *
import pymysql

# Register your models here.
# 每個table一定要有PRIMARY KEY
admin.site.register(CtValueControl)
admin.site.register(CtValueEctoderm)
admin.site.register(CtValueEndoderm)
admin.site.register(CtValueMesendoderm)
admin.site.register(CtValueMesoderm)
admin.site.register(CtValueOther)
admin.site.register(CtValueSelfrenewal)
admin.site.register(FoldChangeEctoderm)
admin.site.register(FoldChangeEndoderm)
admin.site.register(FoldChangeMesendoderm)
admin.site.register(FoldChangeMesoderm)
admin.site.register(FoldChangeSelfrenewal)
admin.site.register(MechanicalParameter)
admin.site.register(Score)
