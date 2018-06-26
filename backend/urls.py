from django.conf.urls import url,include
from rest_framework import routers, serializers, viewsets

from . import views
from .models import Pictures

class PicturesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Pictures
        fields=('id','primarykey','filename','path','fullpath','selectcount','last_used','removed','favorite')

class PicturesViewSet(viewsets.ModelViewSet):
    queryset=Pictures.objects.all()
    serializer_class=PicturesSerializer

router=routers.DefaultRouter()
router.register(r'listapi',PicturesViewSet)


urlpatterns = [
    url(r'^',include(router.urls)),
    url(r'^$', views.list),
    url(r'list$', views.list),
    url(r'build', views.build),
    url(r'select/$', views.select),
    url(r'select/force/$',views.select, {'force': '1'}),
]
