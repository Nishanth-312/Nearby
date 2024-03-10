# app.py

from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Route to render index.html
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle finding nearby cities
@app.route('/find_nearby_cities', methods=['POST'])
def find_nearby_cities():
    location = request.json.get('location')

    # Making a request to the OSM API
    osm_api_url = f"https://nominatim.openstreetmap.org/search?format=json&q={location}"
    response = requests.get(osm_api_url)
    cities_data = response.json()

    nearby_cities = [city['display_name'] for city in cities_data]

    return jsonify(nearby_cities)

if __name__ == '__main__':
    app.run(debug=True)
