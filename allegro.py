import zeep

wsdl = 'https://webapi.allegro.pl.webapisandbox.pl/service.php?wsdl'
client = zeep.Client(wsdl=wsdl)
filter_type = client.get_type('{urn:SandboxWebApi}FilterOptionsType')
filter_array = client.get_type('{urn:SandboxWebApi}ArrayOfFilteroptionstype')

usrLogin = 'mkhslovensko'
usrPass = 'ee7465d2d5B2ebe1'
webApiKey = 'see7465d'
countryCode = 1
localVersion = 0
categoryCode1 = 77935L #Literatura
categoryCode2 = 98553L #Bilety
categoryCode = 3L #Motoryzacja
categoryCode3 = 253498L #Akcesoria samochdowe

filteroptions = filter_array(filter_type(filterId = 'category', filterValueId = categoryCode3))
try:
	#print(client.service.doLogin(usrLogin, usrPass, countryCode, webApiKey, localVersion))
	#print(client.service.doGetCountries(countryCode, webApiKey))
	#print(client.service.doGetCatsDataLimit(countryCode, localVersion, webApiKey, 1))
	#print(client.service.doGetSellFormFieldsForCategory(webApiKey, countryCode, categoryCode))
	print(client.service.doGetItemsList(webApiKey, countryCode, filterOptions = filteroptions))
	#print('test')
except zeep.exceptions.Fault as error:
	detail = error.detail
	print(error.code)
	print('---')
	print(error.message)
	print('---')
	print(error)
