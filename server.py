from flask import Flask, render_template
import random 
import datetime as dt
import requests
app = Flask(__name__)


@app.route("/")
def home_HTML():
    return "<h1>type any name in the path</h1>"


@app.route('/<name>')
def guess(name):
    curent_year = dt.date.today().year
    random_number = random.randint(1, 10)

    def name_age(name):
        url = "https://api.agify.io?"

        headers = {
            "name": name
        }

        response = requests.get(url, headers)
        data = response.json()
        return data['age']

    def name_gender(name):
        url = 'https://api.genderize.io?'

        headers = {
            'name': name
        }

        response = requests.get(url, headers)
        data = response.json()
        return data['gender']


    return render_template('index.html', num=random_number, year=curent_year, age=name_age(name), gender=name_gender(name), name=name)

@app.route('/blog')
def blog():
    url = 'https://api.npoint.io/c790b4d5cab58020d391'
    respons = requests.get(url)
    all_posts = respons.json()

    return render_template('blog.html', posts=all_posts)

 
if __name__ == "__main__":
    app.run(debug=True)

