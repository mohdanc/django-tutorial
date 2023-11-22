'''polls/admin'''
from django.contrib import admin
from .models import Question, Choice

class ChoicesInline(admin.StackedInline):
    '''A'''
    model = Choice
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    '''A'''
    inlines = [ChoicesInline]

# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
