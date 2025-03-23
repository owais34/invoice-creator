import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER_PATH = os.path.join(BASE_DIR, "uploads")
db_path = os.path.join(BASE_DIR, 'invoice_creator.db')
DATABASE_URI = f"sqlite:///{db_path}"
IS_DEV_ENVIRONMENT = False
PORT = int(os.getenv("PORT", "5000"))
if os.getenv("DEBUG", "false").lower() == "true":
    IS_DEV_ENVIRONMENT = True
