from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from .serializer import EmailSeriliazer
from .models import Emails
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from django.core.mail import send_mail
# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_email(request):
    emails = Emails.objects.all()
    serializer = EmailSeriliazer(emails,many=True)
    return Response(serializer.data)

@api_view(['POST'])

def add_email(request):
    data = request.data
    seriliazer = EmailSeriliazer(data=data)
    if seriliazer.is_valid():
        if Emails.objects.filter(email=data['email']).exists():
            return Response({'data':'already exists'},status=status.HTTP_400_BAD_REQUEST)
        
        Emails.objects.create(
            email = data['email']
        )
        return Response({'data':'email added ok'})
    else:
        return Response(seriliazer.errors)
    
@api_view(['POST'])
def Send_Email(request):
    # Extract emails and message from the request
    emails = request.data.get('emails', [])
    subject = request.data.get('subject', '')
    message = request.data.get('message', '')

    print(f"Emails: {emails}, Subject: {subject}, Message: {message}")

    if not emails or not message:
        print("Missing emails or message")
        return Response({"error": "Please provide at least one email and a message."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        print("Sending email...")
        send_mail(
            subject,
            message,
            'ibendaikha9@gmail.com',  # Sender email
            emails,  # Recipients list
            fail_silently=False,
        )
        print("Email sent successfully")
        return Response({"success": "Emails sent successfully!"}, status=status.HTTP_200_OK)
    except Exception as e:
        print(f"Error: {str(e)}")
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
