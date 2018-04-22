import zeep

wsdl = 'https://webapi.allegro.pl.webapisandbox.pl/service.php?wsdl'
client = zeep.Client(wsdl=wsdl)
filter_type = client.get_type('{urn:SandboxWebApi}FilterOptionsType')
filter_array = client.get_type('{urn:SandboxWebApi}ArrayOfFilteroptionstype')

# Local imports...
from app.constants import ALLEGRO_WSDL, ALLEGRO_WEBAPI_KEY, ALLEGRO_COUNTRY

class Category():
    category_list = []

    def __init__(self):
        try:
            self.category_list = client.service.doGetCatsData(ALLEGRO_COUNTRY,
                                                              0,
                                                              ALLEGRO_WEBAPI_KEY)
        except zeep.exceptions.Fault as error:
            detail = error.detail
            print(error.code)
            print('---')
            print(error.message)
            print('---')
            print(error)

    def load_category(self, categoryCode):
        category = []
        for item in self.category_list.catsList.item:
            if item.catParent == categoryCode:
                category.append(item)
        return category

    def load_items_list(self, categoryCode):
        items = []
        filteroptions = filter_array(filter_type(filterId = 'category',
                                                 filterValueId = categoryCode))
        try:
            response = client.service.doGetItemsList(ALLEGRO_WEBAPI_KEY,
                                                     ALLEGRO_COUNTRY, filterOptions =
                                                     filteroptions, resultSize
                                                    = 10)
            if response.itemsList:
                for item in response.itemsList.item:
                    items.append(item)
        except zeep.exceptions.Fault as error:
            print(error.message)
        return items

    def load_items_list_all(self, categoryCode):
        filteroptions = filter_array(filter_type(filterId = 'category',
                                                 filterValueId = categoryCode))
        try:
            response = client.service.doGetItemsList(ALLEGRO_WEBAPI_KEY,
                                                     ALLEGRO_COUNTRY, filterOptions =
                                                     filteroptions, resultSize
                                                    = 20)
        except zeep.exceptions.Fault as error:
            print(error.message)
        return response
