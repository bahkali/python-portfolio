from flask import Flask, render_template, send_from_directory, url_for
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

#for older browser
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/img'),'tech_electronics_icon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == "__main__":
    app.run()