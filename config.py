from dotenv import load_dotenv
import os
load_dotenv()
DB_HOST=os.getenv('DB_HOST','localhost')
DB_USER=os.getenv('DB_USER','root')
DB_PASS=os.getenv('DB_PASS','aaryan123')
DB_NAME=os.getenv('DB_NAME','usermgmt')
DB_PORT=int(os.getenv('DB_PORT','3306'))
STREAMLIT_PORT=int(os.getenv('STREAMLIT_PORT','8501'))
