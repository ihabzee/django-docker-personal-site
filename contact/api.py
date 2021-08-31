from .models import Contact
from rest_framework import routers, serializers, viewsets
from rest_framework.exceptions import APIException


# Serializers define the API representation.
class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact 
        fields = ['uuid', 'subject', 'email', 'content']

# ViewSets define the view behavior.
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

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
