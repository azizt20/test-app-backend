from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
import json
from drf_yasg.utils import swagger_auto_schema
from .serializers import *
from .models import *


class UserModelAdminViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated, ]


class TestModelAdminViewSet(viewsets.ModelViewSet):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticated, ]


class QuestionModelAdminViewSet(viewsets.ModelViewSet):
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, ]


class OptionModelAdminViewSet(viewsets.ModelViewSet):
    queryset = OptionModel.objects.all()
    serializer_class = OptionSerializer
    permission_classes = [IsAuthenticated, ]


class AnswerModelAdminViewSet(viewsets.ModelViewSet):
    queryset = AnswerModel.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, ]


class ResultModelAdminViewSet(APIView):

    @swagger_auto_schema(
        operation_id='result',
        operation_description="Result View",
        # request_body=RegistrationSerializer(),
        responses={
            '200': ResultSerializer()
        },
    )
    def get(self, request):
        data = ResultModel.objects.filter(student=request.user)
        serializer = ResultSerializer(data, many=True)
        return Response(data=serializer.data)
    
    @swagger_auto_schema(
        operation_id='resultPost',
        operation_description="Result Post View",
        request_body=ResultPostSerializer(),
        responses={
            '200': ResultSerializer()
        },
    )
    def post(self, request):
        test = TestModel.objects.get(id=request.data['testId'])
        # answers = json.loads(request.data['results'])
        answers = request.data['results']

        question_list = QuestionModel.objects.filter(test=test)
        score = 0
        
        for i, v in enumerate(question_list):    
            opt = OptionModel.objects.filter(question=v, isAnswer=True)
            if v.type == 2:
                
                if opt[0].option == answers[i]:
                    score += 1
            else:
                list_me = []
                for ll in opt:
                    list_me.append(ll.id)
                
                if answers[i].sort() == list_me.sort():
                    score += 1

        data = ResultModel.objects.create(student=request.user, test=test, score=score)
        serializer = ResultSerializer(data)
        return Response(data=serializer.data)



class RegistrationView(APIView):

    # def get(self, request):
    #     serializer = RegistrationSerializer()
    #     return ResponseSuccess(data=serializer.data, request=request.method)
    @swagger_auto_schema(
        operation_id='registration',
        operation_description="registration",
        request_body=RegistrationSerializer(),
        responses={
            '200': RegistrationSerializer()
        },
    )
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
           
            user = serializer.save()
            access_token = AccessToken().for_user(user)
            refresh_token = RefreshToken().for_user(user)

            return Response(data={
                "refresh": str(refresh_token),
                "access": str(access_token),
                **serializer.data
            })
         
        else:
            return Response(data=serializer.errors)

