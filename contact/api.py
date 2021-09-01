from .models import Contact
from rest_framework import routers, serializers, viewsets
from rest_framework.exceptions import APIException
from django.core.mail import send_mail
from rest_framework.response import Response

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


# Serializers define the API representation.
class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact 
        fields = ['uuid', 'subject', 'email', 'content']

# ViewSets define the view behavior.
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def create(self, request, *args, **kwargs): 
        message = Mail(
            from_email='contactme@zeedia.link',
            to_emails='ihab.zeedia@gmail.com',
            subject=request.data['subject'],
            html_content=request.data['content'])
        message.reply_to = request.data['email']
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message) 
        return super().create(request)

        # use pass to prevent deleting the record
    def list(self, request, *args, **kwargs):
        raise APIException('Not allowed')
    
            # use pass to prevent deleting the record
    def retrieve(self, request, *args, **kwargs):
        raise APIException('Not allowed')

        # use pass to prevent deleting the record
    def destroy(self, request, *args, **kwargs):
        raise APIException('Not allowed')

    def update(self, request, *args, **kwargs):
        raise APIException('Not allowed')
