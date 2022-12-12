from rest_framework import serializers
from .models import UserModel, TestModel, QuestionModel, OptionModel, AnswerModel, ResultModel


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ['id','username', 'first_name', 'last_name', 'password', 'PINFL', 'birthday']
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True},
        }
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class OptionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OptionModel
        fields = ['id', 'question', 'isAnswer', 'option']
        extra_kwargs = {
            'id': {'read_only': True},
            'isAnswer': {'write_only': True},
        }


class OptionAnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OptionModel
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    optis = OptionAnswerSerializer(source='options', many=True, read_only=True)
    class Meta:
        model = QuestionModel
        fields = ['id', 'test', 'question', 'type', 'optis']
        extra_kwargs = {
            'id': {'read_only': True},
            # 'optis': {'read_only': True},
        }

class Question2Serializer(serializers.ModelSerializer):
    optis = OptionSerializer(source='options', many=True, read_only=True)
    class Meta:
        model = QuestionModel
        fields = ['id', 'test', 'question', 'type', 'optis']
        extra_kwargs = {
            'id': {'read_only': True},
            # 'optis': {'read_only': True},
        }


class TestSerializer(serializers.ModelSerializer):
    quests = Question2Serializer(source='questions', many=True, read_only=True)
    class Meta:
        model = TestModel
        fields = ['id', 'name', 'quests']
        extra_kwargs = {
            'id': {'read_only': True},
            # 'quests': {'read_only': True},
        }


class AnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AnswerModel
        fields = '__all__'


class ResultSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ResultModel
        fields = '__all__'
    

class ResultPostSerializer(serializers.Serializer):
    testId = serializers.IntegerField()
    results = serializers.CharField()
