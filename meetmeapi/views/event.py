"""View module for handling requests about event types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from meetmeapi.models import Event, EventUser, MeetMeUser


class EventView(ViewSet):
    """Level up event types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single event type

        Returns:
            Response -- JSON serialized event type
        """
        try:
            event = Event.objects.get(pk=pk)
            serializer = EventSerializer(event)
            return Response(serializer.data)
        except Event.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 

    def list(self, request):
        """Handle GET requests to get all event types

        Returns:
            Response -- JSON serialized list of event types
        """
        events = Event.objects.all()
        current_user = self.request.query_params.get('user')
        if current_user is not None:
            events = events.filter(organizer=current_user)
        # Set the `joined` property on every event
        for event in events:
            # Check to see if the meet_user is in the attendees list on the event
            event.joined = MeetMeUser in event.attendees.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        meet_user = MeetMeUser.objects.get(user=request.auth.user)

        event = Event.objects.create(
            name=request.data["name"],
            description=request.data["description"],
            date=request.data["date"],
            time=request.data["time"],
            organizer=meet_user,
            address=request.data["address"],
            coordinates=request.data["coordinates"]
        )
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for an event

        Returns:
            Response -- Empty body with 204 status code
        """

        event = Event.objects.get(pk=pk)
        event.description = request.data["description"]
        event.date = request.data["date"]
        event.time = request.data["time"]
        event.address = request.data["address"]
        event.name = request.data["name"]
        event.coordinates = request.data["coordinates"]
        event.save()

        organizer = MeetMeUser.objects.get(pk=request.data["organizer"])
        event.organizer = organizer
        event.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        event = Event.objects.get(pk=pk)
        event.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['post'], detail=True)
    def signup(self, request, pk):
        """Post request for a user to sign up for an event"""
    
        meet_user = MeetMeUser.objects.get(user=request.auth.user)
        event = Event.objects.get(pk=pk)
        event.attendees.add(meet_user)
        return Response({'message': 'User added.'}, status=status.HTTP_201_CREATED)
    
    @action(methods=['delete'], detail=True)
    def leave(self, request, pk):
        """Delete request to leave an event"""
    
        meet_user = MeetMeUser.objects.get(user=request.auth.user)
        event = Event.objects.get(pk=pk)
        event.attendees.remove(meet_user)
        return Response({'message': 'User deleted.'}, status=status.HTTP_204_NO_CONTENT)


class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for event types
    """
    class Meta:
        model = Event
        fields = ('id', 'name', 'description', 'date', 'time', 'organizer', 'attendees', 'joined', 'address', 'coordinates')
        depth = 2