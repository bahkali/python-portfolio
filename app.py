from flask import Flask, render_template, send_from_directory, url_for, request
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict();
        print(data)
        return 'Form submitted'
    else:
        return 'something went wrong, try again!'

#for older browser
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/img'),'tech_electronics_icon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == "__main__":
    app.run()