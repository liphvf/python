from django.contrib import admin

from .models import Course

#configura o que vai ser visto no admin na lista de cursos,
#nesse caso a coluna name, slug, data de inicio e de criação
#diz também o que vai ser pesquisado(aparecerá um campo de busca, que ele busca por nome e slug)
class CurseAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'start_date', 'created_at']
	search_fields = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)} # gera o slug ja povoado

# dicionar CurseAdmin que é uma casse que modela o admin do curse
admin.site.register(Course, CurseAdmin)
