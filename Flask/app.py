from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route("/home.html/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        city = request.form['city']
        country = request.form['country']
        api_key = "b9a78f9fcc0a59020e3cef2a9fa20008"
        weather_url = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},{country}&units=imperial')
        weather_data = weather_url.json()
        temp = round((weather_data['main']['temp']-32)/1.8)
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        return render_template("weatherrep.html", temp=temp, humidity=humidity, wind_speed=wind_speed, city=city)
    return render_template("home.html")