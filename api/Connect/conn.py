import xmlrpc.client

url = 'http://localhost:8069'
db = 'dev'
username = 'saadrcaa@gmail.com'
password = 'sk76wBPSFFs8VSZ'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
output = common.version()

print(output)

uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
models.execute_kw(db, uid, password, 'res.partner', 'check_access_rights', ['read'], {'raise_exception': False})

#Search
partners = models.execute_kw(db, uid, password, 'crm.lead', 'search', [[]],
                             {'offset': 0, 'limit': 50})

count = models.execute_kw(db, uid, password, 'crm.lead', 'search_count', [[]])

ids = models.execute_kw(db, uid, password, 'crm.lead', 'search', [[]],
                        {'limit': 1})

[record] = models.execute_kw(db, uid, password, 'crm.lead', 'read', [ids])

searchWithFields = models.execute_kw(db, uid, password, 'crm.lead', 'read', [ids],
                                    {'fields': ['name', 'partner_id', 'partner_name', 'email_from', 'website',
                                                'team_id', 'kanban_state', 'create_date', 'write_date', 'priority']})

listingRecordsWithAttribs = models.execute_kw(db, uid, password, 'crm.lead', 'fields_get', [],
                                   {'attributes': ['string', 'help', 'type']})

listingRecordAllAttribs = models.execute_kw(db, uid, password, 'crm.lead', 'fields_get', [])


#Search And Read
searchAndRead = models.execute_kw(db, uid, password, 'crm.lead', 'search_read', [[]],
                                  {'fields': ['name', 'partner_id', 'partner_name', 'email_from', 'website', 'team_id',
                                              'kanban_state', 'create_date', 'write_date', 'priority'], 'limit': 5})

#create partner
id = models.execute_kw(db, uid, password, 'crm.lead', 'create', [{'name': 'New Lead By API',
                                                                  'email_from': 'saadrcaa@gmail.com',
                                                                  'website': False, 'kanban_state': 'yellow'}])

#Update Partner
models.execute_kw(db, uid, password, 'crm.lead', 'write', [[id], {'name': 'Newer Lead By API'}])

#searchById
searchById = models.execute_kw(db, uid, password, 'crm.lead', 'name_get', [[id]])

#deleteById
models.execute_kw(db, uid, password, 'crm.lead', 'unlink', [[id]])

#DelUsersearchById
delUser = models.execute_kw(db, uid, password, 'crm.lead', 'search', [[['id', '=', id]]])

print(partners)
print(count)
print(len(record))
print(searchWithFields)
print(listingRecordsWithAttribs)
print(listingRecordAllAttribs)
print(searchAndRead)
print(id)
print(searchById)
print(delUser)
