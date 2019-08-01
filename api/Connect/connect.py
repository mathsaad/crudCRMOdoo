import xmlrpc.client
from xmlrpc.client import ServerProxy


class Odoo():
    ids: object
    idLead: object
    output: object
    uid: object
    object: ServerProxy
    common: ServerProxy
    url = 'http://localhost:8069'
    db = 'dev'
    username = 'saadrcaa@gmail.com'
    password = 'sk76wBPSFFs8VSZ'
    commonUrl = "{}/xmlrpc/2/common".format(url)

    def _init_(self, url, db, username, password, commonUrl):
        self.url = url
        self.db = db
        self.username = username
        self.password = password
        self.commonUrl = commonUrl

    def authenticateOdoo(self):
        common = xmlrpc.client.ServerProxy(self.commonUrl)
        self.output = common.version()
        self.uid = common.authenticate(self.db, self.username, self.password, {})
        self.object = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(self.url))

    def checkAcess(self):
        return self.object.execute_kw(self.db, self.uid, self.password, 'crm.lead', 'check_access_rights', ['read'],
                                      {'raise_exception': False})

    def search(self):
        return self.object.execute_kw(self.db, self.uid, self.password, 'crm.lead', 'search', [[]],
                                      {'offset': 0, 'limit': 50})

    def count(self):
        return self.object.execute_kw(self.db, self.uid, self.password, 'crm.lead', 'search_count', [[]])

    def catchFirstLead(self):
        self.ids = self.object.execute_kw(self.db, self.uid, self.password, 'crm.lead', 'search', [[]], {'limit': 1})
        [record] = self.object.execute_kw(self.db, self.uid, self.password, 'crm.lead', 'read', [self.ids])
        return record

    def searchWithFiedls(self):
        return self.object.execute_kw(self.db, self.uid, self.password, 'crm.lead', 'read', [self.ids],
                                      {'fields': ['name', 'partner_id', 'partner_name', 'email_from', 'website',
                                                  'team_id', 'kanban_state', 'create_date', 'write_date', 'priority']})

    def listingRecordWithAttribs(self):
        return self.object.execute_kw(self.db, self.uid, self.password, 'crm.lead', 'fields_get', [],
                                      {'attributes': ['string', 'help', 'type']})

    def listingRecordWithAllAttribs(self):
        return self.object.execute_kw(self.db, self.uid, self.password, 'crm.lead', 'fields_get', [])

    def searchAndRead(self):
        return self.object.execute_kw(self.db, self.uid, self.password, 'crm.lead', 'search_read', [[]],
                                      {'fields': ['name', 'partner_id', 'partner_name', 'email_from', 'website',
                                                  'team_id',
                                                  'kanban_state', 'create_date', 'write_date', 'priority'], 'limit': 5})

    def createLead(self):
        self.idLead = self.object.execute_kw(self.db, self.uid, self.password, 'crm.lead', 'create',
                                             [{'name': 'New Lead By API', 'email_from': 'saadrcaa@gmail.com',
                                               'website': False, 'kanban_state': 'green',
                                               'priority': '3', 'write_date': '10-02-2019'}])
        return self.idLead

    def updateLead(self):
        return self.object.execute_kw(self.db, self.uid, self.password, 'crm.lead', 'write',
                                      [[self.idLead], {'name': 'Newer Lead By API'}])

    def searchById(self, idlead=None):
        return self.object.execute_kw(self.db, self.uid, self.password, 'crm.lead', 'name_get', [[idlead]])

    def deleteById(self, idlead=None):
        self.object.execute_kw(self.db, self.uid, self.password, 'crm.lead', 'unlink', [[idlead]])
        delUser = self.object.execute_kw(self.db, self.uid, self.password, 'crm.lead', 'search',
                                         [[['id', '=', idlead]]])
        return delUser


od = Odoo()
od.authenticateOdoo()
print(od.output)
print(od.uid)

print(od.search())
print(od.count())
print(len(od.catchFirstLead()))
print(od.searchWithFiedls())
print(od.listingRecordWithAttribs())
print(od.listingRecordWithAllAttribs())
print(od.searchAndRead())
print(od.createLead())
