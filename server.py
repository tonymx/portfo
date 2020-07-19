from flask import Flask, render_template, url_for,request,redirect
import csv

app = Flask(__name__)
#print(__name__)

@app.route('/')
def welcome_page():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

def write_to_file(data):
	with open('database.txt',mode='a') as database:
		name=data["name"]
		email=data["email"]
		message=data["message"]
		file=database.write(f'\n{name},{email},{message}')
		database.close()

def write_to_csv(data):
	with open('database.csv','a',newline='\n') as database2:
		name=data["name"]
		email=data["email"]
		message=data["message"]
		csv_writer=csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([name,email,message])
		database2.close()

@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
	if request.method == 'POST':
		data=request.form.to_dict()
		write_to_csv(data)
		return redirect('/index.html')
	else:
		return 'something went wrong'
	
