import requests
#Making a sample request to the API

def test_API(string):
    url = "http://localhost:3000/"
    requestAvailability = requests.get(url +
    string)
    print requestAvailability.text

#request 1:
print "\nSample Request 1"
test_API("Dave/-9.6556550/-3.4545444/4.95499550/3.5455449")
#request 2:
print "\nSample Request 2"
test_API("Jeff/-9.6556551/-3.4545441/4.95499551/3.5455441")
