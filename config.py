import os
import getpass


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
EMAIL_HOST = os.getenv("EMAIL_HOST", "")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 465))
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "")
# EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "")   # <--- Remove this line!
RECIPIENTS = os.getenv("RECIPIENTS", "").split(",")  # comma-separated emails
