# app.py
from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Mock data for marine life
marine_life = [
    {"id": 1, "name": "Clownfish", "description": "A small, vibrant fish known for its symbiotic relationship with sea anemones.", "image": "clownfish.jpg"},
    {"id": 2, "name": "Great White Shark", "description": "A large predatory fish known for its fearsome reputation.", "image": "great_white_shark.jpg"},
    {"id": 3, "name": "Sea Turtle", "description": "A gentle reptile that has been around for millions of years.", "image": "sea_turtle.jpg"},
    {"id": 4, "name": "Jellyfish", "description": "A gelatinous creature that drifts through the ocean currents.", "image": "jellyfish.jpg"},
    {"id": 5, "name": "Coral", "description": "A marine organism that forms large underwater structures called coral reefs.", "image": "coral.jpg"},
]

@app.route('/')
def home():
    return "Welcome to DivingVision API!"

@app.route('/marine_life', methods=['GET'])
def get_marine_life():
    return jsonify(marine_life)

@app.route('/marine_life/<int:life_id>', methods=['GET'])
def get_marine_life_detail(life_id):
    life = next((item for item in marine_life if item["id"] == life_id), None)
    if life:
        return jsonify(life)
    else:
        return jsonify({"error": "Marine life not found"}), 404

@app.route('/random_marine_life', methods=['GET'])
def get_random_marine_life():
    return jsonify(random.choice(marine_life))

@app.route('/search_marine_life', methods=['GET'])
def search_marine_life():
    query = request.args.get('query', '').lower()
    results = [item for item in marine_life if query in item['name'].lower() or query in item['description'].lower()]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)

