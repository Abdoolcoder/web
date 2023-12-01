from flask import Flask, render_template,request
import csv
app = Flask(__name__)

@app.route('/')
def hello():
	return render_template('index.html')
def write_to_csv(data):
	email = data['email']
	name = data['name']
	comment = data['comment']
	print(name)
	print(email)
	with open('database.csv' , mode='a') as database:
		csv_writer = csv.writer(database,delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,name,comment])
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method=='POST':
		data = request.form.to_dict()
		
		write_to_csv(data)
		return 'submited'
	else:
		return 'oopppsss'
