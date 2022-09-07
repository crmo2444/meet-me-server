from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from meetmeapi.models.meetmeuser import MeetMeUser

class MeetMeUserView(ViewSet):
    """Level up meet_user types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single meet_user type

        Returns:
            Response -- JSON serialized meet_user type
        """
        try:
            meet_user = MeetMeUser.objects.get(pk=pk)
            serializer = MeetMeUserSerializer(meet_user)
            return Response(serializer.data)
        except meet_user.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 

    def list(self, request):
        """Handle GET requests to get all meet_users

        Returns:
            Response -- JSON serialized list of meet_users
        """
        meet_users = MeetMeUser.objects.all()
        current_user = self.request.query_params.get('user')
        if current_user is not None:
            meet_users = meet_users.filter(user=current_user)

        serializer = MeetMeUserSerializer(meet_users, many=True)
        return Response(serializer.data)

    def destroy(self, request, pk):
        meet_user = MeetMeUser.objects.get(pk=pk)
        meet_user.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class MeetMeUserSerializer(serializers.ModelSerializer):
    """JSON serializer for meet_users
    """
    class Meta:
        model = MeetMeUser
        fields = ('id', 'user')
        depth = 2