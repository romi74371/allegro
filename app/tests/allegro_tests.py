from nose.tools import assert_true
import requests
import zeep

# Local imports...
from app.constants import ALLEGRO_WSDL, ALLEGRO_WEBAPI_KEY, ALLEGRO_COUNTRY

client = zeep.Client(wsdl=ALLEGRO_WSDL)
filter_type = client.get_type('{urn:SandboxWebApi}FilterOptionsType')
filter_array = client.get_type('{urn:SandboxWebApi}ArrayOfFilteroptionstype')

def test_request_response():
    # Send a request to the API server and store the response.
    response = requests.get(ALLEGRO_WSDL)

    # Confirm that the request-response cycle completed successfully.
    assert_true(response.ok)

def test_get_category():
    try:
        response = client.service.doGetCatsData(ALLEGRO_COUNTRY, 0,
                                                ALLEGRO_WEBAPI_KEY)
        #print(find(lambda item: item.catParent == 0, response.catsList.item))
        for item in response.catsList.item:
            if item.catParent == 3:
                print(item)
        #for item in response.catsList.item:
    except zeep.exceptions.Fault as error:
        detail = error.detail
        print(error.code)
        print('---')
        print(error.message)
        print('---')
        print(error)


def test_get_item_list():
    filteroptions = filter_array(filter_type(filterId = 'category',
        filterValueId = 253498))
    try:
        response = client.service.doGetItemsList(ALLEGRO_WEBAPI_KEY,
                    ALLEGRO_COUNTRY, filterOptions = filteroptions)
        #print(response.itemsList.item)
        assert_true(len(response.itemsList.item)>0)
    except zeep.exceptions.Fault as error:
        detail = error.detail
        print(error.code)
        print('---')
        print(error.message)
        print('---')
        print(error)
