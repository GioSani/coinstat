from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import  get_user_model
from django.utils import timezone
import datetime
jwt_payload_handler             = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler              = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler    = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER
expire_delta = api_settings.JWT_REFRESH_EXPIRATION_DELTA

User = get_user_model()

class UserLoginSerializer(serializers.Serializer):

    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(style={'input_type': 'password'})





    def authenticate(self, **kwargs):
        return authenticate(self.context['request'], **kwargs)

    def get_token_response(self, obj):
        user = obj
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        context =self.context
        request = context['request']

        response = jwt_response_payload_handler(token, user,request=context['request'])
        #print response
        return response

    def get_expires(self, obj):
        return timezone.now() + expire_delta - datetime.timedelta(seconds=200)



    def get_token(self, obj):
        user = obj
        payload = jwt_payload_handler(user)
        token   = jwt_encode_handler(payload)
        return token

    def _validate_email(self, email, password):
        user = None

        if email and password:
            user = self.authenticate(email=email, password=password)
        else:
            msg = _('Must include "email" and "password".')
            raise exceptions.ValidationError(msg)

        return user








class UserRegisterSerializer(serializers.ModelSerializer):
    password            = serializers.CharField(style={'input_type':'password'},write_only=True)
    password2          = serializers.CharField(style={'input_type':'password'},write_only=True)
    token               = serializers.SerializerMethodField(read_only=True)
    expires             = serializers.SerializerMethodField(read_only=True)
    token_response      = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2',
            'token',
            'expires',
            'token_response',
        ]
        extra_kwargs = {'password':{'write_only':True},'password2':{'write_only':True}}

    def get_token_response(self, obj):
        user = obj
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        context =self.context
        request = context['request']

        response = jwt_response_payload_handler(token, user,request=context['request'])
        #print response
        return response

    def get_expires(self, obj):
        return timezone.now() + expire_delta - datetime.timedelta(seconds=200)



    def validate_email(self, value):
        #print value
        qs = User.objects.filter(email__iexact=value)
        #print qs
        if qs.exists():
            raise serializers.ValidationError('user with this email is already exists')
        return value

    def validate_username(self, value):
        qs  = User.objects.filter(username__iexact = value)
        if qs.exists():
            raise serializers.ValidationError('user with this username is already exists')
        return value
    def get_token(self, obj):
        user = obj
        payload = jwt_payload_handler(user)
        token   = jwt_encode_handler(payload)
        return token

    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')
        if password != password2:
            raise serializers.ValidationError('password must match')
        return data

    def create(self, validated_data):
        print validated_data.get('username')
        user_obj = User(
            username = validated_data.get('username'),
            email    = validated_data.get('email')
        )
        user_obj.set_password(validated_data.get('password'))
        user_obj.save()
        return user_obj
