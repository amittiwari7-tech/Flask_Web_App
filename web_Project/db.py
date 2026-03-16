import os
import pymysql
from dotenv import load_dotenv

load_dotenv()

# हम Flask-MySQLdb का इस्तेमाल नहीं करेंगे क्योंकि वह इंस्टॉल नहीं हो रही
# हम सीधा PyMySQL का इस्तेमाल करेंगे जो बहुत आसान है
class MySQL:
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.app = app

    @property
    def connection(self):
        # यह लाइन डेटाबेस से सीधा कनेक्शन बनाएगी
        return pymysql.connect(
            host=os.getenv('dataBase_URL'),
            user=os.getenv('database_User'),
            password=os.getenv('database_Password'),
            database=os.getenv('database_Name'),
            port=int(os.getenv('database_Port', 3306)),
            cursorclass=pymysql.cursors.DictCursor # इससे डेटा Dictionary के रूप में मिलेगा
        )

# ऑब्जेक्ट बनाएँ
mysql = MySQL()

def init_db(app):
    mysql.init_app(app)
    return mysql