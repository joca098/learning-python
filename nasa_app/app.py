from flask import Flask, render_template, jsonify
import requests 

app = Flask(__name__) 

api_url = "https://api.nasa.gov/planetary/apod"
api_key = 'm2u3zxriUlYvSM3p4OzFXDKUh7DgVsSiwyM1rAcY'

app.route('/')

def index():
    params = {
        'api_key': api_key
    }
    
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()

        return render_template('index.html', data=data)
    else:
        return f"Error {response.status_code}"
    
    if __name__ == '__main__':
        app.run(debug=True)