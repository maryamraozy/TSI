from flask import Flask, jsonify, Request, render_template
from flask_restful import Resource, Api
import requests


app = Flask(__name__, template_folder='templates', static_folder='static')
api = Api(app)

@app.route("/", methods=['GET'])
def test():
    response = requests.post(
    url="https://auth.predicthq.com/OHYyH4VUxGp_gAoaIT_5XIV0LRNjPDz7e6l_Qfl1",
    auth=("nQOEv6ApsAw", "OHYyH4VUxGp_gAoaIT_5XIV0LRNjPDz7e6l_Qfl1"),
    headers={
      "Accept": "application/json"
    },
    data={
        "grant_type": "client_credentials",
        "scope": "account events places"
    }
)


    #response = requests.get(
    #url="https://api.predicthq.com/v1/events/calendar/",
    #headers={
     # "Authorization": "Bearer $OHYyH4VUxGp_gAoaIT_5XIV0LRNjPDz7e6l_Qfl1",
      #"Accept": "application/json"
    #},
    #params={
     # "country": "GB",
      #"place.scope": "birmingham",
      #"location_around.origin": "52.47867° N,-1.90848° E"
    #}
#)
    print(response.json())
    return render_template("/home.html")









if __name__ == "__main__":
    app.run(debug=True)

#id = nQOEv6ApsAw
#secret = PRCPQhV2ucyw3GS9ayRBfayP4evy4Zowp9GVHGAm


#token = OHYyH4VUxGp_gAoaIT_5XIV0LRNjPDz7e6l_Qfl1