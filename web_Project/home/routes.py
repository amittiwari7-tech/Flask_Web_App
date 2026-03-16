from flask import Blueprint,url_for,render_template,request,redirect,flash,session
from web_Project.utils.utl import login_required
from web_Project.db import mysql
import os
from werkzeug.utils import secure_filename

home_bp = Blueprint('home',__name__,template_folder='templates',static_folder='static',static_url_path='/home/static')


@home_bp.route('/showUserData')
@login_required
def showHome():
    cursor = mysql.connection.cursor()
    query = "SELECT * FROM user_info"
    cursor.execute(query)
    users = cursor.fetchall()
    print(users)
    return render_template('home.html', user=users)



@home_bp.route('/submitData',methods=(['GET','POST']))

def submitData():
    if request.method == 'POST':
        name = request.form.get('userName')
        email = request.form.get('userEmail')
        age = request.form.get('userAge')
        imageFile = request.files.get('image')
        print(imageFile)
        if imageFile:
            fileName = secure_filename(imageFile.filename)
            print(fileName.rsplit('.', 1))
            filePath = os.path.join('static/uploads', fileName)
            imageFile.save(filePath)
        else:
            fileName = None
            

        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO user_info (Name, Email,Age,Image) VALUES (%s, %s,%s,%s)', (name, email,age,fileName))
        mysql.connection.commit()
        cursor.close()
        flash('Data submitted successfully!', 'success')
    return redirect(url_for('home.showHome'))

#delete user Data from Database

@home_bp.route('/deleteData',methods=['POST'])
def deleteRow():
    if request.method =='POST':
        email = request.form.get('userEmail')
        print(email)
        cur = mysql.connection.cursor()
        cur.execute("Delete from user_info where Email = %s",(email,))
        mysql.connection.commit()
        flash('Data deleted successfully!', 'success')
    return redirect(url_for('home.showHome'))    


#update user Data from Database

@home_bp.route('/updateData', methods=['GET', 'POST'])
def updateData():
  
    formName = formEmail = formAge = ""

    if request.method == 'GET':
       
        formName = request.args.get('name', '')
        formEmail = request.args.get('email', '')
        formAge = request.args.get('age', '')
        
    if request.method == 'POST':
      
        name = request.form.get('name')
        email = request.form.get('email')
        age = request.form.get('age')
        imageFile = request.files.get('image')
        
       
        if imageFile:
            fileName = secure_filename(imageFile.filename)
            filePath = os.path.join('static/uploads', fileName)
            imageFile.save(filePath)
        else:
            fileName = None 

       
        cursor = mysql.connection.cursor()
        cursor.execute('UPDATE user_info SET Name=%s, Age=%s, Image=%s WHERE Email=%s', 
                       (name, age, fileName, email))
        mysql.connection.commit()
        cursor.close()
        
        flash('Data Updated successfully!', 'success')
        
        return redirect(url_for('home.showHome')) 

    
    return render_template('update.html', name=formName, email=formEmail, age=formAge)