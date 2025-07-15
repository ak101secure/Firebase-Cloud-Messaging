import firebase_admin
from firebase_admin import credentials, messaging
import datetime

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

message = messaging.Message(
    notification=messaging.Notification(
        title="Demo Notification",
        body="Hello! This is a test notification from Firebase Admin Python.",
    ),
    android=messaging.AndroidConfig(
        ttl=datetime.timedelta(seconds=3600),
        priority='normal',
        notification=messaging.AndroidNotification(
            icon='demo_icon',
            color='#f45342'
        ),
    ),
    apns=messaging.APNSConfig(
        payload=messaging.APNSPayload(
            aps=messaging.Aps(badge=1),
        ),
    ),
    topic='demo-topic',
)

response = messaging.send(message)
print('Successfully sent message:', response)