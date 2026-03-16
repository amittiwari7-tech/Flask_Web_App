from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os


load_dotenv()  # Load environment variables from .env file

mysql = MySQL()
def init_db(app):
    app.config['MYSQL_HOST'] = os.getenv('dataBase_URL')
    app.config['MYSQL_USER'] = os.getenv('database_User')
    app.config['MYSQL_PASSWORD'] = os.getenv('database_Password')
    app.config['MYSQL_DB'] = os.getenv('database_Name')
    app.config['MYSQL_PORT'] = int(os.getenv('database_Port',3306))

    return mysql.init_app(app) 