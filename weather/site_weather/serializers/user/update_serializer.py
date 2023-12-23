# from rest_framework import serializers



# class UserUpdateSerializers(serializers.Serializer):
    
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField(max_length=5)
#     currency = serializers.CharField()
#     balance = serializers.IntegerField()
#     price = serializers.IntegerField()
#     owner = serializers.IntegerField(read_only=True)
#     # owner = serializers.SlugRelatedField(
#     #     many=False,
#     #     read_only=True,
#     #     slug_field='username'
#     # )

#     def create(self, validated_data):
#         return WalletSerial.objects.create(**validated_data)
    
#     # Будет нормально работать только на put - ???
#     # def update (self,instance,validated_data):
#     #     instance.name = validated_data.get('name', instance.name)
#     #     instance.currency = validated_data.get('currency', instance.currency)
#     #     instance.balance = validated_data.get('balance', instance.balance)
#     #     instance.price = validated_data.get('price', instance.price)

#     def update(self,instance,validated_data):
#         for attr, value in validated_data.items():
#             setattr(instance, attr, value)
#         instance.save()
#         return instance