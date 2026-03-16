import os
import pymysql
from flask_mysqldb import MySQL
from dotenv import load_dotenv

# Render के लिए सबसे ज़रूरी फिक्स
pymysql.install_as_MySQLdb()

load_dotenv() 

mysql = MySQL()

def init_db(app):
    app.config['MYSQL_HOST'] = os.getenv('dataBase_URL')
    app.config['MYSQL_USER'] = os.getenv('database_User')
    app.config['MYSQL_PASSWORD'] = os.getenv('database_Password')
    app.config['MYSQL_DB'] = os.getenv('database_Name')
    app.config['MYSQL_PORT'] = int(os.getenv('database_Port', 3306))

    mysql.init_app(app) # यह ऐप को कॉन्फ़िगर करता है
    return mysql # यहाँ 'mysql' ऑब्जेक्ट रिटर्न करें