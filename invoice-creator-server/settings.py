import os

basedir = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER_PATH = os.path.join(basedir, "uploads")
db_path = os.path.join(basedir, 'invoice_creator.db')
DATABASE_URI = f"sqlite:///{db_path}"
IS_DEV_ENVIRONMENT = False
PORT = int(os.getenv("PORT", "5000"))
if os.getenv("DEBUG", "true").lower() == "true":
    IS_DEV_ENVIRONMENT = True
