from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import status
from ArithmenticOperations.models import Operation
from rest_framework.decorators import api_view,APIView
from .serializers import OperationSerializer


class OperationAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = OperationSerializer
    def post(self, request):
        serializer = OperationSerializer(data=request.data)
        if serializer.is_valid():
            num1 = serializer.validated_data['num1']
            num2 = serializer.validated_data['num2']
            operation = serializer.validated_data['operation']
            result = None
            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                if num2 == 0:
                    return Response({"error": "Cannot divide by zero"}, status=status.HTTP_400_BAD_REQUEST)
                result = num1 / num2
            return Response({"result": result}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
