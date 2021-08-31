from .models import Section
from rest_framework import routers, serializers, viewsets
from rest_framework.exceptions import APIException


# Serializers define the API representation.
class SectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Section 
        fields = ['id', 'title', 'type', 'content']

# ViewSets define the view behavior.
class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.filter(active=True).order_by('type')
    serializer_class = SectionSerializer

        # use pass to prevent deleting the record
    def destroy(self, request, *args, **kwargs):
        raise APIException('Not allowed')

    def create(self, request, *args, **kwargs):
        raise APIException('Not allowed')

    def update(self, request, *args, **kwargs):
        raise APIException('Not allowed')
