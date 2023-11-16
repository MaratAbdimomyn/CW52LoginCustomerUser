from rest_framework import serializers
from .models import *
from rest_framework.serializers import ModelSerializer

class CustomersSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    confirm_password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = Customer
        fields = ['first_name', 'second_name', 'last_name', 'username', 'image', 'email', 'password', 'confirm_password']

    def validate(self, data):
        if len(data['username']) < 5:
            raise serializers.ValidationError("Username must be longer than 5 characters")
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = Customer.objects.create_user(**validated_data)
        return user

class ListCustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'second_name', 'last_name', 'username', 'image', 'email']

class UpdateCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'second_name', 'last_name', 'username', 'image', 'email']

class LoginCustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['username', 'password']

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name', 'price', 'description')