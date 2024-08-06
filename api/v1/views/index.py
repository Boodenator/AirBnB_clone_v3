#!/usr/bin/python3
"""
Status of endpoint
"""
from models import storage
from flask import Flask
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def status():
    """
    Return status of JSON
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def count():
    """
    number of types of objects to retrieve
    """
    return jsonify({"amenities": storage.count("Amenity"),
                    "cities": storage.count("City"),
                    "places": storage.count("Place"),
                    "reviews": storage.count("Review"),
                    "states": storage.count("State"),
                    "users": storage.count("User")})
