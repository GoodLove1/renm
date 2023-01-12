import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "12635510")

API_HASH = os.environ.get("API_HASH", "da59e4e56ec4fe35af603bd30208ecc5")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5896030795:AAFLuJeLSEMuoGSG8JupUqGCcpSbgkX9Mvs") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1001861393412") 

DB_NAME = os.environ.get("DB_NAME","cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://thorlord:thorlord@cluster0.9iffkxw.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1130215726').split()]

