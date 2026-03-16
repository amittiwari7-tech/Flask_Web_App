from flask import Flask
from web_Project.db import init_db
from web_Project.auth.routes import auth_bp
from web_Project.home.routes import home_bp
import secrets
from flask_jwt_extended import JWTManager

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = "jgfhgjhdfgjhgjbkDHKHJK4545WDHJ"  
jwt = JWTManager(app)  
app.secret_key = secrets.token_hex(16)  
init_db(app)
app.register_blueprint(auth_bp)
app.register_blueprint(home_bp)

if __name__ == '__main__':
    app.run(debug=True)
    