from flask import Flask, request, render_template, jsonify
import requests
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/get_place', methods = ['POST'])
def get_place():
    url = "https://ai-weather-by-meteosource.p.rapidapi.com/find_places"
    query = {
        'text': str(request.form['textInput']),
        'language': 'en'
    }
    headers = {
        'X-RapidAPI-Key': 'bbf3da1751mshcb3aa47a6db2663p1fdc0cjsne2dee69d5b5e',
        'X-RapidAPI-Host': 'ai-weather-by-meteosource.p.rapidapi.com'
    }
    data = requests.get(url, headers = headers, params= query)
    adm_area1 = data.json()[0]['adm_area1']
    country = data.json()[0]['country']
    lat = data.json()[0]['lat']
    lon = data.json()[0]['lon']
    # return data.json()[0]['adm_area1']
    # return jsonify(data.json())
    return f"Place you entered belongs to {adm_area1}, Country is {country}, Latitude is {lat}, Longitude is {lon} !"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 7000)