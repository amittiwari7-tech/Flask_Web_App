from flask import Flask , Blueprint,url_for,render_template,request,redirect,flash,session,jsonify
from werkzeug.security import generate_password_hash,check_password_hash
from ..db import mysql  
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth',__name__,template_folder='templates',static_folder='static',static_url_path='/auth/static')

@auth_bp.route('/',methods=['GET','POST'])

def login():
    if(request.method == 'POST'):
        username = request.form.get('email')
        password = request.form.get('password')
        
        cur = mysql.connection.cursor()
        
        query = "Select * from users where Email = %s"
        cur.execute(query,(username,))
        user = cur.fetchone()
        print(user)
        cur.close()
        
        if user and user[3] == password:  # Assuming password is the 4th column
           
            session['user'] = user[1]  # Store username in session
            flash('Login successful!', 'success')
         
        else:
            flash('Invalid username or password', 'error')
    return render_template('authenticate/login.html')

#register user             
            
@auth_bp.route('/register',methods=['GET','POST'])

def signUp():
    
    if request.method == 'POST':
          userName = request.form['name']
          email = request.form['email']
          password = request.form['password']
          hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
          cur = mysql.connection.cursor()
          #check Email already exist
          check_query = "SELECT * FROM users WHERE Email = %s"
          cur.execute(check_query, (email,))
          existing_user = cur.fetchone()
          
          if existing_user:
                flash('Email already exists. Please choose a different one.', 'error')
              
          else:  
          #insert Data in Database  
            query = "INSERT INTO users (Name, Email, Password) VALUES (%s, %s, %s)"
            cur.execute(query, (userName, email, password))
            mysql.connection.commit()
            cur.close()
            flash('Registration successful! Please log in.', 'success')
               
    return render_template('authenticate/signup.html')       
          
   
   
 
 # Forget Password
 
@auth_bp.route('/forget_password', methods=['GET', 'POST'])
def forget_password():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        cur = mysql.connection.cursor()
        
        query = "UPDATE users SET Password = %s WHERE Email = %s"
        cur.execute(query, (password, email))
        mysql.connection.commit()   
        cur.close()
        flash('Password reset instructions have been sent to your email.', 'success')
        
    return render_template('authenticate/forgetpassword.html')
    
    
    
    
@auth_bp.route('/logout')
def logout():
      session.pop('user', None)  # Remove user from session
      return redirect(url_for('auth.login'))        