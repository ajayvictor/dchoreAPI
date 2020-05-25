from flask import Flask, redirect, url_for, request, jsonify
app = Flask(__name__) 
  
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

      user = {
	"name" : "Ajay",
	"username" : username,
        "email" : "test@test.com",
        "gender" : "Male",
	"category" : "User"
	}

      print(username)
      print(worker_username)
      print(date)
      print(time)

      return jsonify(
        status=True,
	status_message="Yeah!! Cool, Booking Success",
	user=user    	
	)
   else: 
      user = request.args.get('nm') 
      return redirect(url_for('success',name = user)) 
 



@app.route('/workers_bookings',methods = ['POST', 'GET']) 
def workers_bookings(): 
   if request.method == 'POST': 
      username = request.form['username'] 

      print(username)

      users = [{
	"name" : "Ajay",
        "email" : "test@test.com",
        "location" : "Alappuzha",
	"mobile" : "12345678",
        "date" : "12-07-2020",
        "time" : "06:30 PM"
	}]

      print(users)

      return jsonify(
        status=True,
	status_message="Yeah!! Cool, Booking Success",
	users=users    	
	)
   else: 
      user = request.args.get('nm') 
      return redirect(url_for('success',name = user)) 



@app.route('/workers_booked_data',methods = ['POST', 'GET'])
def workers_booked_data(): 
   if request.method == 'POST': 
      username = request.form['username'] 

      workers = [{
	"name" : "Ponnappan",
	"mobile" : 1234567890,
        "job" : "Coconut Tree Climber",
        "age" : 50,
        "experience" : 10,
	"place" : "Alleppey",
	"date" : "13-01-2020",
	"time" : "10:30 AM"
	},
	{
	"name" : "Thankappan",
	"mobile" : 1234567890,
        "job" : "Plumber",
        "age" : 50,
        "experience" : 10,
	"place" : "Alleppey",
	"date" : "12-01-2020",
	"time" : "11:30 AM"
	}	
	]


      return jsonify(
        status=True,
	status_message="Yeah!! Cool",
	workers=workers
	)





@app.route('/workers_data',methods = ['POST', 'GET']) 
def workers_data(): 
   if request.method == 'POST': 
      username = request.form['username'] 

      workers = [{
	"name" : "Ponnappan",
	"mobile" : 1234567890,
        "job" : "Coconut Tree Climber",
        "age" : 50,
        "experience" : 10,
	"place" : "Alleppey"
	},
	{
	"name" : "Thankappan",
	"mobile" : 1234567890,
        "job" : "Plumber",
        "age" : 50,
        "experience" : 10,
	"place" : "Alleppey"
	},
	{
	"name" : "Vasoottan",
	"mobile" : 1234567890,
        "job" : "Welder",
        "age" : 50,
        "experience" : 10,
	"place" : "Alleppey"
	},
	{
	"name" : "Rajappan",
	"mobile" : 1234567890,
        "job" : "Contractor",
        "age" : 50,
        "experience" : 10,
	"place" : "Alleppey"
	}
	]


      return jsonify(
        status=True,
	status_message="Yeah!! Cool",
	workers=workers
	)



@app.route('/login',methods = ['POST', 'GET']) 
def login(): 
   if request.method == 'POST': 
      username = request.form['username'] 
      password = request.form['password'] 

      user = {
	"name" : "test",
	"username" : username,
        "email" : "test@test.com",
        "gender" : "Male",
	"category" : "User",
        "location" : "Alleppey",
	}

      print(user)

      return jsonify(
        status=True,
	status_message="Yeah!! Cool",
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

      user = {
	"name" : "test",
	"username" : username,
        "email" : "test@test.com",
        "gender" : "Male",
	"category" : "Worker",
        "location" : "Alleppey",
	}

      print(user)

      return jsonify(
        status=True,
	status_message="Yeah!! Cool",
	user=user    	
	)
   else: 
      user = request.args.get('nm') 
      return redirect(url_for('success',name = user)) 



@app.route('/worker_signup',methods = ['POST', 'GET']) 
def worker_signup(): 
   if request.method == 'POST': 
      username = request.form['username'] 
      email = request.form['email'] 
      password = request.form['password'] 
      category = request.form['category'] 
      gender = request.form['gender'] 
      experience = request.form['experience'] 
      age = request.form['age'] 
      location = request.form['location'] 

      user = {
	"name" : "Ajay",
	"username" : username,
        "email" : email,
        "gender" : gender,
        "category" : "Worker",
        "location" : location,
	}

      print(user)

      return jsonify(
        status=True,
	status_message="Yeah!! Cool",
	user=user    	
	)
   else: 
      user = request.args.get('nm') 
      return redirect(url_for('success',name = user)) 





@app.route('/signup',methods = ['POST', 'GET']) 
def signup(): 
   if request.method == 'POST': 
      username = request.form['username'] 
      email = request.form['email'] 
      password = request.form['password'] 
      location = request.form['location'] 
      gender = request.form['gender'] 
      category = request.form['category'] 
      

      user = {
	"name" : "Ajay",
	"username" : username,
        "email" : email,
        "gender" : gender,
        "location" : location,
        "category" : "User",
	}

      print(user)

      return jsonify(
        status=True,
	status_message="Yeah!! Cool",
	user=user    	
	)
   else: 
      user = request.args.get('nm') 
      return redirect(url_for('success',name = user)) 

  
if __name__ == '__main__': 
   app.run(debug = True,host='0.0.0.0')
