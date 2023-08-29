from routes import app,employees,logs,seq
from flask import request, jsonify, Response , send_file
from bson.json_util import dumps,loads
import json
from bson import ObjectId
import base64
from datetime import datetime
# from helpers import token_required, token_generate
from flask import Blueprint

home_route = Blueprint('home_route', __name__)


@home_route.route('/get_all')
def index():
    arg = request.args['filter']
    if arg == 'all':
        logs_list = logs.find()    
    else :
        logs_list = logs.find({'action':arg})
    employee_list = employees.find()
    log=[]
    emp=[]
    for x in logs_list:
        data={}
        data['_id'] = str(x['_id'])
        data['at'] = x['at']
        data['action'] = x['action']
        data['name'] = x['name']
        log.append(data)
    for x in employee_list:
        data={}
        data['_id'] = str(x['_id'])
        emp.append(data)
    return {'logs':log[::-1],'employees':emp}

@home_route.route('/get_employee/<int:emp_id>')
def get_employee(emp_id):
    emp = employees.find_one({"_id": emp_id})
    name = emp['name']
    position = emp['position']
    password = emp['password']
    status = emp['status']
    return {"_id": emp_id, "name": name, "position": position,'password':password,'status':status}


@home_route.route('/add_employee', methods=['POST'])
def add_employee():
    emp = request.json
    name = emp['name']
    position = emp['position']
    password = emp['password']
    status = emp['status']
    sequence_doc = seq.find_one_and_update(
        {"_id": "employeeId"},
        {"$inc": {"seq": 1}},
        upsert=True,
        return_document=True
    )
    # Use the updated sequence number as the new employeeId
    employee_id = sequence_doc["seq"]
    new_employee = {"_id": employee_id, "name": name, "position": position,'password':password,'status':status}
    employees.insert_one(new_employee)
    logs.insert_one({"action": "Added employee", "name": name,'at':datetime.utcnow()})
    return {'message':'success'}

@home_route.route('/update_employee/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    emp = request.json
    name = emp['name']
    position = emp['position']
    password = emp['password']
    status = emp['status']
    employees.update_one({"_id": employee_id}, {"$set": {"name": name, "position": position,"password":password,"status":status}})
    logs.insert_one({"action": "Updated employee", "name": name,'at':datetime.utcnow()})
    
    return {'message':'success'}

@home_route.route('/delete_employee/<int:employee_id>',methods=['DELETE'])
def delete_employee(employee_id):
    employee = employees.find_one({"_id": employee_id})
    name = employee["name"]

    employees.delete_one({"_id": employee_id})
    logs.insert_one({"action": "Deleted employee", "name": name,'at':datetime.utcnow()})
    
    return {'message':'success'}
