from .base import *

SITE_URL = "http://localhost:8000"

if os.environ.get("POSTGRES"):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': 'db',
            'PORT': '5432',
            'USER': 'postgres',
            'NAME': 'postgres',
        }
    }

SLACK_TOKEN = get_env_var("SLACK_TOKEN", True)
SLACK_SIGNING_SECRET = get_env_var("SLACK_SIGNING_SECRET", True)
INCIDENT_CHANNEL_NAME = get_env_var("INCIDENT_CHANNEL_NAME", True)
INCIDENT_BOT_NAME = get_env_var("INCIDENT_BOT_NAME", True)

try:
    INCIDENT_BOT_ID = get_user_id(INCIDENT_BOT_NAME, SLACK_TOKEN)
except:
    INCIDENT_BOT_ID = None

try:
    INCIDENT_CHANNEL_ID = get_channel_id(INCIDENT_CHANNEL_NAME, SLACK_TOKEN)
except:
    INCIDENT_CHANNEL_ID = None
