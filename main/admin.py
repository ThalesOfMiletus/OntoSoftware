from django.contrib import admin

from.models import Professores,Discplina,Aula,Turma

admin.site.register(Professores)
admin.site.register(Discplina)
admin.site.register(Aula)
admin.site.register(Turma)

'''
class ProfessoresAdmin(admin.ModelAdmin):
    list_display=('nome')
    list_editable=('status',)
admin.site.register(Professores,ProfessoresAdmin)
'''
'''
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display=('id','product','price','color','size')
admin.site.register(ProductAttribute)'''