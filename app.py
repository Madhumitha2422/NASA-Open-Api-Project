from flask import Flask, render_template, request
import requests

app = Flask(__name__)


API_KEY = "bKEN0vCDezP6lDqPnf62NIIKeeDZg7rDuUqVC1ot"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        date = request.form['date']
        image_data = get_apod_image(date)
        return render_template('index.html', image_data=image_data)

    return render_template('index.html', image_data=None)

def get_apod_image(date):
    base_url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': API_KEY,
        'date': date
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        image_data = response.json()
        return image_data
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)
