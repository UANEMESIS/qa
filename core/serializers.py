from rest_framework import serializers
from .models import Certificate, Upload
from rest_framework import pagination



# import sys



# reload(sys)
# sys.setdefaultencoding("utf-8")

class UploadSerializer(serializers.ModelSerializer):
    #author = AuthorSerializer(read_only=True)
    class Meta:
        model = Upload
        fields = ('id', 'file', 'name')




class CertificateSerializer(serializers.ModelSerializer):
    #author = AuthorSerializer(read_only=True)
    class Meta:
        model = Certificate
        fields = '__all__'

# class PaginatedProductSerializer(pagination.PaginationSerializer):
#     """
#     Serializes page objects of user querysets.
#     """
#     class Meta:
#         object_serializer_class = ProductSerializer