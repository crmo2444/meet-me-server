from datetime import date
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from meetmeapi.models.savedaddress import SavedAddress
from meetmeapi.models.meetmeuser import MeetMeUser

class SavedAddressView(ViewSet):
    """Level up saved_address types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single saved_address type

        Returns:
            Response -- JSON serialized saved_address type
        """
        try:
            saved_address = SavedAddress.objects.get(pk=pk)
            serializer = SavedAddressSerializer(saved_address)
            return Response(serializer.data)
        except saved_address.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 

    def list(self, request):
        """Handle GET requests to get all saved_addresss

        Returns:
            Response -- JSON serialized list of saved_addresss
        """
        saved_addresses = SavedAddress.objects.all()
        current_user = self.request.query_params.get('user')
        if current_user is not None:
            saved_addresses = saved_addresses.filter(user=current_user)

        serializer = SavedAddressSerializer(saved_addresses, many=True)
        return Response(serializer.data)

    def destroy(self, request, pk):
        """delete a saved result location"""
        saved_address = SavedAddress.objects.get(pk=pk)
        saved_address.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def create(self, request):
        """Handle POST operations"""
        user = MeetMeUser.objects.get(user=request.auth.user)

        saved_address = SavedAddress.objects.create(
            user=user,
            name=request.data["name"],
            address=request.data["address"],
            coordinates=request.data["coordinates"]
            )
        serializer = SavedAddressSerializer(saved_address)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class SavedAddressSerializer(serializers.ModelSerializer):
    """JSON serializer for saved_addresss
    """
    class Meta:
        model = SavedAddress
        fields = ('id', 'user', 'name', 'address', 'coordinates')
        depth = 2