from rest_framework import serializers
from django.contrib.auth.models import User

'''
serializer to register user and 
overriding save() method to validate user input

'''
class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type' : 'password'}, write_only=True)   # 
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password' : {'write_only' : True}
        }
    
    # save() method to register the user and check the valid password and unique mail id
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        # validating password
        if password != password2:
            raise serializers.ValidationError('Passwords must match.')
        
        # validating unique email id
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError('Email already exists.')
        
        # saving the user object
        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(password)
        account.save()
        
        return account