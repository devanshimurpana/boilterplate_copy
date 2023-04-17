from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


technicians = Blueprint('technicians', __name__)

#create technician profile 
@technicians.route('/technician', methods=['POST'])
def add_company():
    the_data = request.json
    current_app.logger.info(the_data)
    technician_id = the_data['technician_id']
    last_name = the_data['last_name']
    first_name = the_data['first_name']
    query = 'insert into Technician values("'
    query += str(technician_id) + '", "'
    query += last_name + '", "'
    query += first_name + '")'
    current_app.logger.info(query)
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    return 'Success'


# Updates company status to closed (unavailible) given company name
# when that company has accepetd a bid from PE_Firm 
@technicians.route('/company_status', methods=['PUT'])
def update_company_status():
    the_data = request.json
    company_name = the_data['company_name']
    current_app.logger.info(the_data)
    query = 'update Company set company_status = 0 where company_name = "' + company_name + '"'
    current_app.logger.info(query)
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    return 'Success'

# Gets companies that exist  
@technicians.route('/company/<company_id>', methods=['GET'])
def get_companies(company_id):
    cursor = db.get_db().cursor()
    cursor.execute('select * from Company where company_id = {0}'.format(company_id))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# Approve company legitimacy 
def update_company_status():
    the_data = request.json
    company_id = the_data['company_id']
    current_app.logger.info(the_data)
    query = 'update Company set company_status = 0 where company_name = "' + company_name + '"'
    current_app.logger.info(query)
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    return 'Success'
