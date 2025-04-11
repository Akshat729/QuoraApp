from rest_framework.decorators import api_view
from user_app.api.serializers import RegistrationSerializer
from rest_framework.response import Response


'''
function to register the user
'''
@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

'''
function for logout functionality
'''
@api_view(['POST',])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response('Logout successfuly!!',status=200)