from ..Connect.connect import Odoo


class crmLeadService():

    def __init__(self):
        od = Odoo()
        od.authenticateOdoo()

