from flask import jsonify, request
from app import app
from app.services import crm_lead


crmLead = crm_lead.CrmLead()

@app.route('/search')
def search():
    result = crmLead.searchAndRead()
    return jsonify(result), 200

@app.route('/add/lead', methods=['POST'])
def createLead():
    lead = request.get_json();
    result = crmLead.createLead(lead)
    return jsonify(result), 201
    

    # {'name': 'New Lead By API', 'email_from': 'saadrcaa@gmail.com',
    #                                            'website': False, 'kanban_state': 'green',
    #                                            'priority': '3', 'write_date': '10-02-2019'}