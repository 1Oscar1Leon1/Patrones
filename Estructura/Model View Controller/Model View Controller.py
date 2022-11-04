class Model(object):
    services = {
        'Xbox series x': {'Code': '#8952','price': 279.900},
        'PS5': {'Code': '#1126','price': 369.900},
        'Nintendo SWITCH': {'Code': '#4574','price': 191.000 },
    }
class View(object):
    def list_services(self, services):
        for svc in services:
            print(svc, " ")
    def list_pricing(self, services):
        for svc in services:
            print("Code", Model.services[svc]['Code'],
                  svc, "in total you pay $",
                  Model.services[svc]['price'])
class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View()
    def get_services(self):
        services = self.model.services.keys()
        return self.view.list_services(services)
    def get_pricing(self):
        services = self.model.services.keys()
        return self.view.list_pricing(services)
class Client(object):
    con = Controller()
    print("Services Provided:")
    con.get_services()
    print("Pricing for Services:")
    con.get_pricing()