from django.contrib import admin
from .models import *


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'question']


class TestAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class OptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'isAnswer', 'option']


admin.site.register(UserModel)
admin.site.register(TestModel, TestAdmin)
admin.site.register(QuestionModel, QuestionAdmin)
admin.site.register(OptionModel, OptionAdmin)
admin.site.register(AnswerModel)
admin.site.register(ResultModel)
# Register your models here.
