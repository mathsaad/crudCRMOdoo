from app import app
from app.connect import conn

class CrmLead():

    od = conn.Odoo()
    od.authenticateOdoo()
    objectOdoo = od.objectOdoo
    object = objectOdoo


    def search(self):
        return self.object.execute_kw(self.od.db, self.od.uid, self.od.password, 'crm.lead', 'search', [[]],
                                      {'offset': 0, 'limit': 50})

    def count(self):
        return self.object.execute_kw(self.od.db, self.od.uid, self.od.password, 'crm.lead', 'search_count', [[]])

    def catchFirstLead(self):
        self.ids = self.object.execute_kw(self.od.db, self.od.uid, self.od.password, 'crm.lead', 'search', [[]], {'limit': 1})
        [record] = self.object.execute_kw(self.od.db, self.od.uid, self.od.password, 'crm.lead', 'read', [self.ids])
        return record

    def searchWithFiedls(self):
        return self.object.execute_kw(self.od.db, self.od.uid, self.od.password, 'crm.lead', 'read', [self.ids],
                                      {'fields': ['name', 'partner_id', 'partner_name', 'email_from', 'website',
                                                  'team_id', 'kanban_state', 'create_date', 'write_date', 'priority']})

    def listingRecordWithAttribs(self):
        return self.object.execute_kw(self.od.db, self.od.uid, self.od.password, 'crm.lead', 'fields_get', [],
                                      {'attributes': ['string', 'help', 'type']})

    def listingRecordWithAllAttribs(self):
        return self.object.execute_kw(self.od.db, self.od.uid, self.od.password, 'crm.lead', 'fields_get', [])

    def searchAndRead(self):
        return self.object.execute_kw(self.od.db, self.od.uid, self.od.password, 'crm.lead', 'search_read', [[]],
                                      {'fields': ['name', 'partner_id', 'partner_name', 'email_from', 'website',
                                                  'team_id',
                                                  'kanban_state', 'create_date', 'write_date', 'priority'], 'limit': 5})

    def createLead(self):
        self.idLead = self.object.execute_kw(self.od.db, self.od.uid, self.od.password, 'crm.lead', 'create',
                                             [{'name': 'New Lead By API', 'email_from': 'saadrcaa@gmail.com',
                                               'website': False, 'kanban_state': 'green',
                                               'priority': '3', 'write_date': '10-02-2019'}])
        return self.idLead

    def updateLead(self, idlead):
        return self.object.execute_kw(self.od.db, self.od.uid, self.od.password, 'crm.lead', 'write',
                                      [[idlead], {'name': 'Newer Lead By API'}])

    def searchById(self, idlead):
        return self.object.execute_kw(self.od.db, self.od.uid, self.od.password, 'crm.lead', 'name_get', [[idlead]])

    def deleteById(self, idlead):
        self.object.execute_kw(self.od.db, self.od.uid, self.od.password, 'crm.lead', 'unlink', [[idlead]])
        delUser = self.object.execute_kw(self.od.db, self.od.uid, self.od.password, 'crm.lead', 'search',
                                         [[['id', '=', idlead]]])
        return delUser