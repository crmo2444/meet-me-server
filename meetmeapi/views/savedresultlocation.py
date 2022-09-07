from datetime import date
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from meetmeapi.models.savedresultlocation import SavedResultLocation
from meetmeapi.models.meetmeuser import MeetMeUser

class SavedResultLocationView(ViewSet):
    """Level up saved_result_location types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single saved_result_location type

        Returns:
            Response -- JSON serialized saved_result_location type
        """
        try:
            saved_result_location = SavedResultLocation.objects.get(pk=pk)
            serializer = SavedResultLocationSerializer(saved_result_location)
            return Response(serializer.data)
        except saved_result_location.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 

    def list(self, request):
        """Handle GET requests to get all saved_result_locations

        Returns:
            Response -- JSON serialized list of saved_result_locations
        """
        saved_result_locations = SavedResultLocation.objects.all()
        current_user = self.request.query_params.get('user')
        if current_user is not None:
            saved_result_locations = saved_result_locations.filter(user=current_user)

        serializer = SavedResultLocationSerializer(saved_result_locations, many=True)
        return Response(serializer.data)

    def destroy(self, request, pk):
        """delete a saved result location"""
        saved_result_location = SavedResultLocation.objects.get(pk=pk)
        saved_result_location.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def create(self, request):
        """Handle POST operations"""
        user = MeetMeUser.objects.get(user=request.auth.user)

        saved_result_location = SavedResultLocation.objects.create(
            user=user,
            name=request.data["name"],
            coordinate=request.data["coordinate"],
            distance=request.data["distance"],
            created_on=date.today()
            )
        serializer = SavedResultLocationSerializer(saved_result_location)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class SavedResultLocationSerializer(serializers.ModelSerializer):
    """JSON serializer for saved_result_locations
    """
    class Meta:
        model = SavedResultLocation
        fields = ('id', 'user', 'name', 'coordinate', 'distance', 'created_on')
        depth = 2