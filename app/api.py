from flask import request, jsonify, abort
from app import app
from app.siri import hey_siri

@app.route("/api/", methods=['GET'])
def endpoints():
    """Overview of the API endpoints."""
    return jsonify({'endpoints': endpoints})

@app.route("/api/ask", methods=['POST'])
def ask():
    """"""
    if not request.json or 'query' not in request.json:
        return abort(400)
    query = request.json['query']
    hey_siri(query)
    return jsonify({'query': query})



endpoints = [{"path": "/api/",
              "name": endpoints.__name__,
              "method": "GET",
              "description": endpoints.__doc__},
             {"path": "/api/ask",
              "name": ask.__name__,
              "method": "POST",
              "description": ask.__doc__,
              "data": {"query": "Your query for Siri"}}
             ]

