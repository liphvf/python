from django.db import models


class CourseManager(models.Manager):
	
	#posso mudar de "ou"("|") para "e" ("&")
	def search(self, query):
		return self.get_queryset().filter(models.Q(name__icontains=query)| models.Q(description__icontains=query))

class Course(models.Model):

	name = models.CharField('Nome', max_length=100) #verbose name = é o que aparce para o usuário
	slug = models.SlugField('Atalho', )
	description = models.TextField('Descrição', blank=True) # blank=True quer dizer que o campo não é obrigatorio
	start_date = models.DateField('Data de início', null=True, blank=True) # null= True , diz que pode ser null

	#django não armazena imagens no banco de dados, por isso temos que dar a ele um diretorio físico

	image = models.ImageField(upload_to='courses/images', verbose_name='Imagem', null=True, blank=True)

	#precisa no settings ter um MEDIA_ROOT = ''
	#o upload_to é referente a pasta do media root, ou seja, vai ficar mediaroot/courses/images


	created_at = models.DateTimeField('Criado em', auto_now_add=True) #auto_now_add toda vez que criar um curse ele vai colocar a data atual
	update_at = models.DateTimeField('Atualizado em', auto_now=True) #auto_now, toda vez que for salvo ele altera para a data atual.

	object = CourseManager() 

	def __str__(self):
		return self.name

	# no painel admin aparece esté verbose name, singular e plural.
	class Meta:
		verbose_name='Curso'
		verbose_name_plural = 'Cursos'
		ordering = ['name'] # para ordenar pelo nome de forma ascendente
		ordering = ['-name'] # ordenar decendente