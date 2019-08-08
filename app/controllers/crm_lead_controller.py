from flask import jsonify, request
from app import app
from app.services import crm_lead


crmLead = crm_lead.CrmLead()

@app.route('/search', methods=['GET'])
def search():
    result = crmLead.searchAndRead()
    return jsonify(result), 200

@app.route('/search/<int:idlead>', methods=['GET'])
def searchById(idlead):
    result = crmLead.searchById(idlead)
    return jsonify(result), 200

@app.route('/search/<string:mail>', methods=['GET'])
def searchByMail(mail):
    result = crmLead.searchByEmail(mail)
    return jsonify(result), 200

@app.route('/add/lead', methods=['POST'])
def createLead():
    lead = request.get_json()
    result = crmLead.createLead(lead)
    return jsonify(result), 201
        
@app.route('/update/<int:idlead>', methods=['PUT'])
def updateLead(idlead):
    lead = request.get_json()
    result = crmLead.updateLead(idlead, lead)
    return jsonify(result), 200

@app.route('/delete/<int:idlead>', methods=['DELETE'])
def deleteLead(idlead):
    crmLead.deleteById(idlead)
    return   jsonify({'message': 'Lead deletado com sucesso!'}), 200