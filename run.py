import os
import secrets
from flask import Flask
from flask_jwt_extended import JWTManager
from web_Project.db import init_db
from web_Project.auth.routes import auth_bp
from web_Project.home.routes import home_bp

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = "jgfhgjhdfgjhgjbkDHKHJK4545WDHJ"  
jwt = JWTManager(app)  
app.secret_key = secrets.token_hex(16)  

# db को इनिशियलाइज़ करें
mysql = init_db(app)

app.register_blueprint(auth_bp)
app.register_blueprint(home_bp)

if __name__ == '__main__':
    # Render को '0.0.0.0' होस्ट और 'PORT' एन्वायरमेंट वेरिएबल की ज़रूरत होती है
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False) # प्रोडक्शन में debug=False रखें