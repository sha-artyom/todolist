from rest_framework import serializers

from todolist.bot.models import TgUser


class TgUserSerializer(serializers.ModelSerializer):
    tg_id = serializers.IntegerField(source='chat_id', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = TgUser
        fields = ('username', 'tg_id', 'verification_code', 'user_id')
        read_only_fields = ('username', 'tg_id', 'user_id')
