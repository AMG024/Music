from rest_framework import serializers
from api.music.models import Music


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        #fields = '__all__'
        fields = ('song', 'poster', 'singer', 'Album', 'medium','genre','releasetime','publisher','mark')