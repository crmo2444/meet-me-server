from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from meetmeapi.views.auth import register_user, login_user
from rest_framework import routers
from meetmeapi.views.meetmeuser import MeetMeUserView
from meetmeapi.views.savedaddress import SavedAddressView
from meetmeapi.views.savedresultlocation import SavedResultLocationView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', MeetMeUserView, 'user')
router.register(r'saved_result_locations', SavedResultLocationView, 'data')
router.register(r'saved_address', SavedAddressView, 'data')

urlpatterns = [
    # Requests to http://localhost:8000/register will be routed to the register_user function
    path('register', register_user),
    # Requests to http://localhost:8000/login will be routed to the login_user function
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]