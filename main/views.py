from main import app 
from flask import request, jsonify
from main.db_utils import insertRow, deleteRow, retrieveAllRows

@app.route('/')
def home():
    return("You've set up Flask API Template")

@app.route('/insert', methods=['GET'])
def insert():
    email = request.args.get('listItem')
    insertRow(email, email)
    return("SUCCESSFUL")

@app.route('/delete', methods=['GET'])
def delete():
    email = request.args.get('listItem')
    deleteRow(email, email)
    return("SUCCESSFUL")

@app.route('/retrieve', methods=['GET'])
def retrieve():
    allRows = retrieveAllRows()
    return(jsonify(allRows))