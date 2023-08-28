from django.contrib.auth import authenticate
from .models import Persona
from rest_framework import serializers


class PersonaSerializer(serializers.ModelSerializer):
    """serializer para Persona"""

    class Meta:
        model = Persona
        fields = (
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "edad",
            "sexo",
        )
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    def create(self, validated_data):
        password = validated_data.pop("password")
        
        new_persona = {x: validated_data[x] for x in self.Meta.fields if x != "password"}
        
        user = Persona(**new_persona)
        user.set_password(password)
        user.save()
        return user

class PersonaSerializer(serializers.ModelSerializer):
    """serializer para Persona"""

    class Meta:
        model = Persona
        fields = (
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "edad",
            "sexo",
        )
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}
        
class PersonaViewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Persona
        fields = ['url', 'username', 'email']

class AuthSerializer(serializers.Serializer):
    """serializer para el objeto de autenticacion de Persona"""

    username = serializers.CharField()
    password = serializers.CharField(
        style={"input_type": "password"}, trim_whitespace=False
    )

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        user = authenticate(
            request=self.context.get("request"), username=username, password=password
        )

        if not user:
            msg = "No se ha podido acceder con las credenciales proporcionadas"
            raise serializers.ValidationError(msg, code="authentication")

        attrs["user"] = user
        return
