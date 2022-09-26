from fcm_django.models import FCMDevice
from firebase_admin.messaging import Message, Notification
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser

from notifications.api_admin.serializers import NotificationSerializer
from notifications.models import NotificationMessage


class SendPushNotification(CreateAPIView):
    serializer_class = NotificationSerializer
    queryset = NotificationMessage.objects.all()
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        super().perform_create(serializer)
        message_obj = Message(notification=Notification(**serializer.data))
        FCMDevice.objects.all().send_message(message_obj)