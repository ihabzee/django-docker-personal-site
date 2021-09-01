from .models import Article
from rest_framework import routers, serializers, viewsets
from rest_framework.exceptions import APIException


# Serializers define the API representation.
class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article 
        fields = ['uuid', 'title', 'url', 'description', 'image', 'image_url']

# ViewSets define the view behavior.
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.filter(active=True).order_by('-created_at')
    serializer_class = ArticleSerializer

        # use pass to prevent deleting the record
    def destroy(self, request, *args, **kwargs):
        raise APIException('Not allowed')

    def create(self, request, *args, **kwargs):
        raise APIException('Not allowed')

    def update(self, request, *args, **kwargs):
        raise APIException('Not allowed')
