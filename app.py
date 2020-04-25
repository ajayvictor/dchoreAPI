from flask import Flask, redirect, url_for, request, jsonify
app = Flask(__name__) 
  
@app.route('/success/<name>') 
def success(name): 
   return 'welcome %s' % name 
  


@app.route('/worker_confirm',methods = ['POST', 'GET']) 
def worker_confirm(): 
   if request.method == 'POST': 
      username = request.form['username'] 

      user = {
	"id" : 1,
	"username" : username,
        "email" : "test@test.com",
        "gender" : "Male",
	"category" : "User"
	}

      print(user)

      return jsonify(
        status=True,
	status_message="Yeah!! Cool, Booking Success",
	user=user    	
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
	"id" : 1,
	"username" : username,
        "email" : "test@test.com",
        "gender" : "Male",
	"category" : "User"
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
      gender = request.form['gender'] 
      category = request.form['category'] 

      user = {
	"id" : "1",
	"username" : username,
        "email" : email,
        "gender" : gender,
	"category" : category
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
