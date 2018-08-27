from django.contrib import admin

from .models import Question, Choice

# class ChoiceInline(admin.StackedInline): # Ocupa molt d'espai…
class ChoiceInline(admin.TabularInline): # més compacte
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
