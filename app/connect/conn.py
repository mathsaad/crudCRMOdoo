import xmlrpc.client
from xmlrpc.client import ServerProxy


class Odoo():
    ids: object
    idLead: object
    output: object
    uid: object
    idlead = dict
    objectOdoo: ServerProxy
    common: ServerProxy
    url = 'http://localhost:8069'
    db = 'odoo'
    username = 'saadrcaa@gmail.com'
    password = 'sk76wBPSFFs8VSZ'
    commonUrl = "{}/xmlrpc/2/common".format(url)

    def _init_(self, url, db, username, password, commonUrl, idlead):
        self.url = url
        self.db = db
        self.username = username
        self.password = password
        self.commonUrl = commonUrl
        self.idLead = idlead

    def authenticateOdoo(self):
        common = xmlrpc.client.ServerProxy(self.commonUrl)
        self.output = common.version()
        self.uid = common.authenticate(self.db, self.username, self.password, {})
        self.objectOdoo = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(self.url))

    def checkAcess(self, table=None):
        return self.objectOdoo.execute_kw(self.db, self.uid, self.password, [[table]], 'check_access_rights', ['read'],
                                      {'raise_exception': False})