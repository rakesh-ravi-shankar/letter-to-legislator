import lob
import requests
import json

# Load api keys from local config file
keys = json.load(open('keys.json'))
lob.api_key = keys.lob_api_key
civic_api_key = keys.civic_api_key


# Pull legislator info using the Google Civic api
def get_legislator_info(address):
    payload = {
        'address': address,
        'includeOffices': True,
        'levels': 'country',
        'roles': 'legislatorLowerBody'
    }
    response = requests.get('https://www.googleapis.com/civicinfo/v2/representatives?key='+civic_api_key, params=payload)
    response = response.json()
    return response.get('officials')


# Compose and send a letter using the Lob api
def send_letter():
    letter = lob.Letter.create(
      description = 'Letter to legislator',
      to_address = {
          'name': 'Harry Zhang',
          'address_line1': '185 Berry St',
          'address_line2': '# 6100',
          'address_city': 'San Francisco',
          'address_state': 'CA',
          'address_zip': '94107',
          'address_country': 'US'
      },
      from_address = {
          'name': 'Leore Avidar',
          'address_line1': '185 Berry St',
          'address_line2': '# 6100',
          'address_city': 'San Francisco',
          'address_state': 'CA',
          'address_zip': '94107',
          'address_country': 'US'
      },
      file = 'tmpl_5c64c3094c0e11c',
      merge_variables = {
        'message': 'Harry'
      },
      color = True
    )
    print '\n\nLetter Generation Response:'
    print letter