from django.db import models
from django.contrib.auth.models import AbstractUser
import re
import phonenumbers
from django.core.exceptions import ValidationError


class PhoneValidator:
    requires_context = False

    @staticmethod
    def clean(value):
        return re.sub('[^0-9]+', '', value)

    @staticmethod
    def validate(value):
        try:
            z = phonenumbers.parse("+" + value)
            if not phonenumbers.is_valid_number(z):
                return False
        except:
            return False

        if len(value) != 12 or not value.startswith("998"):
            return False

        return True

    def __call__(self, value):
        if not PhoneValidator.validate(value):
            raise ValidationError("Введенное значение не является номером телефона.")


class UserModel(AbstractUser):
    username = models.CharField(max_length=15, unique=True,
                                validators=[PhoneValidator()])
    PINFL = models.CharField(max_length=100, null=True, blank=True)
    birthday = models.DateField(blank=True, null=True)


class TestModel(models.Model):
    name = models.CharField(max_length=255)


class QuestionModel(models.Model):
    test = models.ForeignKey(TestModel, on_delete=models.CASCADE, null=True, blank=True, related_name='questions')
    question = models.CharField(max_length=255)
    type = models.SmallIntegerField(choices=(
        (1, 'simple'),
        (2, 'text'),
        (3, 'many choose')
    ), default=1, db_index=True)


class OptionModel(models.Model):
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE, null=True, related_name='options')
    option = models.CharField(max_length=255)
    isAnswer = models.BooleanField(default=False)


class AnswerModel(models.Model):
    student = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    answer = models.ForeignKey(OptionModel, on_delete=models.CASCADE)
    extra_answer = models.TextField()
    extra_point = models.SmallIntegerField(default=0)


class ResultModel(models.Model):
    student = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    test = models.ForeignKey(TestModel, on_delete=models.CASCADE, null=True, blank=True)
    score = models.CharField(max_length=50)
