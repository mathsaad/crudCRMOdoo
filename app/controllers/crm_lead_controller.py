from flask import jsonify, request
from app import app
from app.services import crm_lead


crmLead = crm_lead.CrmLead()

@app.route('/search')
def search():
    result = crmLead.searchAndRead()
    return jsonify(result), 200