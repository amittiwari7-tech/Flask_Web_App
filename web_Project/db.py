import os
import pymysql
from dotenv import load_dotenv

# 1. सबसे पहले यह लाइन लिखें (Bridge तैयार करें)
pymysql.install_as_MySQLdb()

# 2. अब Flask-MySQLdb इम्पोर्ट करें (अब यह एरर नहीं देगा)
from flask_mysqldb import MySQL 

load_dotenv() 

mysql = MySQL()

def init_db(app):
    app.config['MYSQL_HOST'] = os.getenv('dataBase_URL')
    app.config['MYSQL_USER'] = os.getenv('database_User')
    app.config['MYSQL_PASSWORD'] = os.getenv('database_Password')
    app.config['MYSQL_DB'] = os.getenv('database_Name')
    
    # Port को सुरक्षित रूप से हैंडल करें
    db_port = os.getenv('database_Port', 3306)
    app.config['MYSQL_PORT'] = int(db_port)

    mysql.init_app(app) 
    return mysql