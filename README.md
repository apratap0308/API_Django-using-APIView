# Create an API in Django | ApiView | 

1. Python manage.py runserver
2. pip install djangorestframework
3. Import rest_framework.views import APIView
4. Create Serializers.py


# serializers.py 

rest_framework.views import APIView    

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(label="Enter Book Id")
    title = serializers.CharField(label="Enter book title")
    author = serializers.CharField(label="Enter Author name")
