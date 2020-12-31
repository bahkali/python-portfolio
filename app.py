from flask import Flask, redirect, render_template, send_from_directory, url_for, request
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict();
        write_to_file(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong, try again!'

#for older browser
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/img'),'tech_electronics_icon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == "__main__":
    app.run()