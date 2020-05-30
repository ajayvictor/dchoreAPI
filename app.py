from flask import Flask, redirect, url_for, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__) 


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'dchore'
app.config['MYSQL_PASSWORD'] = 'dch0re'
app.config['MYSQL_DB'] = 'dchore'

mysql = MySQL(app)


@app.route('/success/<name>') 
def success(name): 
   return 'welcome %s' % name 
  


@app.route('/worker_confirm',methods = ['POST', 'GET']) 
def worker_confirm(): 
   if request.method == 'POST': 
      username = request.form['username'] 
      date = request.form['date'] 
      time = request.form['time'] 
      worker_username = request.form['worker_mobile'] 

      print(username)
      print(worker_username)
      print(date)
      print(time)


      try:
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO bookings(worker_username, consumer_username, date, time, status) VALUES (%s, %s, %s, %s, %s)", (worker_username.split(" ")[1], username, date, time, "Pending"))
        mysql.connection.commit()
        cur.close()
        status=True
        status_message="Successfully Booked"
      except Exception as e:
        print(e)
        if "Duplicate" in str(e):
                status=False
                status_message="Slot not Available!!!"
        else:
                status=False
                status_message="Something Went Wrong!! Please try again!!"


      return jsonify(
        status=status,
	status_message=status_message
	)
   else: 
      user = request.args.get('nm') 
      return redirect(url_for('success',name = user)) 
 


@app.route('/confirm_booking',methods = ['POST', 'GET']) 
def confirm_booking(): 
   if request.method == 'POST': 
      username = request.form['username'] 
      name = request.form['name'] 
      date = request.form['date'] 
      time = request.form['time'] 
      booking_status = request.form['status'] 
      consumer_username = request.form['mobile'] 


      try:
        cur = mysql.connection.cursor()
        cur.execute("UPDATE bookings SET status = '" + booking_status + "' where worker_username = '" + username + "' and consumer_username = '" + username + "' and date = '" + date + "' and time = '" + time + "'")
        mysql.connection.commit()
        cur.close()
        status=True
        status_message= booking_status + " Successfully"
      except Exception as e:
        print(e)
        if "Duplicate" in str(e):
                status=False
                status_message="Slot not Available!!!"
        else:
                status=False
                status_message="Something Went Wrong!! Please try again!!"


      return jsonify(
        status=status,
	status_message=status_message
	)
   else: 
      user = request.args.get('nm') 
      return redirect(url_for('success',name = user)) 



#This is for worker
@app.route('/workers_bookings',methods = ['POST', 'GET']) 
def workers_bookings(): 
   if request.method == 'POST': 
      username = request.form['username'] 

      cursor = mysql.connection.cursor()
      try:
        users=[]
        cursor.execute("SELECT user.name, user.username, user.email, user.gender, user.location, bookings.date, bookings.time, bookings.status FROM user INNER JOIN bookings ON user.username=bookings.consumer_username where bookings.worker_username='" + username + "'")
        data = list(cursor.fetchall())
        print(data)
        if data is None:
                status=False
                status_message="No Bookings!!"
        else:
                status=True
                status_message="Processed!!"
                for item in data:
                        user = {
                                "name" : item[0],
                                "mobile" : item[1],
                                "email" : item[2],
                                "gender" : item[3],
                                "location" : item[4],
                                "date" : item[5],
                                "time" : item[6],
                                "status" : item[7]
                                }
                        users.append(user)
      except Exception as e:
        print(e)
        status=False
        status_message="Something Went Wrong!"

      print(users)

#       users = [{
# 	"name" : "Ajay",
#         "email" : "test@test.com",
#         "location" : "Alappuzha",
# 	"mobile" : "12345678",
#         "date" : "12-07-2020",
#         "time" : "06:30 PM"
# 	}]


      return jsonify(
        status=status,
	status_message=status_message,
	users=users	
	)
   else: 
      user = request.args.get('nm') 
      return redirect(url_for('success',name = user)) 



#This is for user
@app.route('/workers_booked_data',methods = ['POST', 'GET'])
def workers_booked_data(): 
   if request.method == 'POST': 
      username = request.form['username'] 


      cursor = mysql.connection.cursor()
      try:
        cursor.execute("SELECT workers.name, workers.username, workers.profession, workers.age, workers.experience, workers.location, bookings.date, bookings.time, bookings.status FROM workers INNER JOIN bookings ON workers.username=bookings.worker_username where bookings.consumer_username='" + username + "'")
        data = list(cursor.fetchall())
        works=[]
        if data is None:
                status=False
                status_message="No Bookings!!"
        else:
                status=True
                status_message="Processed!!"
                for item in data:
                        work = {
                                "name" : item[0],
                                "mobile" : item[1],
                                "job" : item[2],
                                "age" : item[3],
                                "experience" : item[4],
                                "place" : item[5],
                                "date" : item[6],
                                "time" : item[7],
                                "status" : item[8]
                                }
                        works.append(work)
                        print(works)
      except Exception as e:
        print(e)
        works=[]
        status=False
        status_message="Something Went Wrong!"


#       workers = [{
# 	"name" : "Ponnappan",
# 	"mobile" : 1234567890,
#         "job" : "Coconut Tree Climber",
#         "age" : 50,
#         "experience" : 10,
# 	"place" : "Alleppey",
# 	"date" : "13-01-2020",
# 	"time" : "10:30 AM",
#         "status" : "Pending"
# 	},
# 	{
# 	"name" : "Thankappan",
# 	"mobile" : 1234567890,
#         "job" : "Plumber",
#         "age" : 50,
#         "experience" : 10,
# 	"place" : "Alleppey",
# 	"date" : "12-01-2020",
# 	"time" : "11:30 AM",
#                 "status" : "Confirmed"

# 	}	
# 	]


      return jsonify(
        status=status,
	status_message=status_message,
	workers=works
	)





@app.route('/workers_data',methods = ['POST', 'GET']) 
def workers_data(): 
   if request.method == 'POST': 
      username = request.form['username'] 
      try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * from workers")
        data = list(cursor.fetchall())
        print(data)
        workers=[]
        i=1
        for item in data:
                print(i)
                worker={}
                worker['name'] = item[0]
                worker['mobile'] = item[1]
                worker['job'] = item[4]
                worker['age'] = item[7]
                worker['experience'] = item[5]
                worker['place'] = item[6]
                workers.append(worker)
                i=i+1
        
        status=True
        status_message="Processed!"


      except Exception as e:
        print(e)
        status=False
        status_message="Something Went Wrong!"

#       workers = [{
# 	"name" : "Ponnappan",
# 	"mobile" : 1234567890,
#         "job" : "Coconut Tree Climber",
#         "age" : 50,
#         "experience" : 10,
# 	"place" : "Alleppey"
# 	},
# 	{
# 	"name" : "Thankappan",
# 	"mobile" : 1234567890,
#         "job" : "Plumber",
#         "age" : 50,
#         "experience" : 10,
# 	"place" : "Alleppey"
# 	},
# 	{
# 	"name" : "Vasoottan",
# 	"mobile" : 1234567890,
#         "job" : "Welder",
#         "age" : 50,
#         "experience" : 10,
# 	"place" : "Alleppey"
# 	},
# 	{
# 	"name" : "Rajappan",
# 	"mobile" : 1234567890,
#         "job" : "Contractor",
#         "age" : 50,
#         "experience" : 10,
# 	"place" : "Alleppey"
# 	}
# 	]


      return jsonify(
        status=status,
	status_message=status_message,
	workers=workers
	)



@app.route('/login',methods = ['POST', 'GET']) 
def login(): 
   if request.method == 'POST': 
      username = request.form['username'] 
      password = request.form['password'] 

      cursor = mysql.connection.cursor()
      try:
        cursor.execute("SELECT * from user where Username='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:
                status=False
                status_message="Username or Password is wrong!!"
        else:
                status=True
                status_message="Logged in successfully!!"
                user = {
                        "name" : data[1],
                        "username" : username,
                        "email" : data[2],
                        "gender" : data[4],
                        "category" : "User",
                        "location" : data[5],
                        }
      except Exception as e:
        print(e)
        status=False
        status_message="Something Went Wrong!"

      return jsonify(
        status=status,
	status_message=status_message,
	user=user    	
	)
   else: 
      user = request.args.get('nm') 
      return redirect(url_for('success',name = user)) 
 


@app.route('/worker_login',methods = ['POST', 'GET']) 
def worker_login(): 
   if request.method == 'POST': 
      username = request.form['username'] 
      password = request.form['password'] 

      
      cursor = mysql.connection.cursor()
      try:
        cursor.execute("SELECT * from workers where Username='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:
                status=False
                status_message="Username or Password is wrong!!"
                user = None
        else:
                status=True
                status_message="Logged in successfully!!"
                user = {
                                "name" : data[0],
                                "username" : username,
                                "email" : data[2],
                                "gender" : data[8],
                                "category" : "Worker",
                                "location" : data[6],
                        }
      except Exception as e:
        print(e)
        status=False
        status_message="Something Went Wrong!"

      return jsonify(
        status=status,
	status_message=status_message,
	user=user    	
	)
   else: 
      user = request.args.get('nm') 
      return redirect(url_for('success',name = user)) 



@app.route('/worker_signup',methods = ['POST', 'GET']) 
def worker_signup(): 
   if request.method == 'POST': 
      username = request.form['username'] 
      name = request.form['name'] 
      email = request.form['email'] 
      password = request.form['password'] 
      category = request.form['category'] 
      gender = request.form['gender'] 
      experience = request.form['experience'] 
      age = request.form['age'] 
      location = request.form['location'] 
      profession = request.form['category'] 

      user = {
	"name" : name,
	"username" : username,
        "email" : email,
        "gender" : gender,
        "category" : "Worker",
        "location" : location,
	}

      try:
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO workers(name, username, email, password, profession, experience, age, location, gender) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (name, username, email, password, profession, experience, age, location, gender))
        mysql.connection.commit()
        cur.close()
        status=True
        status_message="Successfully Registered"
      except Exception as e:
        print(e)
        if "Duplicate" in str(e):
                status=False
                status_message="Worker already Exists!!!"
        else:
                status=False
                status_message="Something Went Wrong!! Please try again!!"

      return jsonify(
        status=status,
	status_message=status_message,
	user=user    	
	)
   else: 
      user = request.args.get('nm') 
      return redirect(url_for('success',name = user)) 





@app.route('/signup',methods = ['POST', 'GET']) 
def signup(): 
   if request.method == 'POST': 
      username = request.form['username'] 
      name = request.form['name'] 
      email = request.form['email'] 
      password = request.form['password'] 
      location = request.form['location'] 
      gender = request.form['gender'] 
      category = request.form['category'] 
      

      user = {
	"name" : name,
	"username" : username,
        "email" : email,
        "gender" : gender,
        "location" : location,
        "category" : "User",
	}



      try:
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user(name, username, email, password, location, gender) VALUES (%s, %s, %s, %s, %s, %s)", (name, username, email, password, location, gender))
        mysql.connection.commit()
        cur.close()
        status=True
        status_message="Successfully Registered"
      except Exception as e:
        print(e)
        if "Duplicate" in str(e):
                status=False
                status_message="User already Exists!!!"
        else:
                status=False
                status_message="Something Went Wrong!! Please try again!!"


      return jsonify(
        status=status,
	status_message=status_message,
	user=user    	
	)
   else: 
      user = request.args.get('nm') 
      return redirect(url_for('success',name = user)) 

  
if __name__ == '__main__': 
   app.run(debug = True,host='0.0.0.0')
