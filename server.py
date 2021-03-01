from flask import Flask, render_template, request, redirect, jsonify
import csv

app = Flask(__name__)
print(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n {email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',')
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thanks.html')
    else:
        return 'something is wrong'


@app.route('/json')
def get_json():
    people = [{'name': 'Alice', 'birth-year': 1986},
              {'name': 'Bob', 'birth-year': 1985}]
    return jsonify(people)


'''
@app.route('/works.html')
def works():
    return render_template('works.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/components.html')
def components():
    return render_template('components.html')


@app.route('/about.html')
def about():
    return render_template('about.html')
    
    '''
