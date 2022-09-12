import dotenv
import os

dotenv.load_dotenv()

TG_API_TOKEN = os.getenv('API')
TG_API_URL = f'https://api.telegram.org/bot{TG_API_TOKEN}/'
url_joke = os.getenv('url_joke')
