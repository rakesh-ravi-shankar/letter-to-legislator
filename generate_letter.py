import lob
import requests
import json

# Load api keys from local config file
keys = json.load(open('keys.json'))
lob.api_key = keys.get('lob_api_key')
civic_api_key = keys.get('civic_api_key')


# Ask user for input args
def parse_input_args():
    from_address = {}
    message_payload = ''

    print 'Enter from address details:'
    from_address['name'] = raw_input('Enter name: ')
    from_address['address_line1'] = raw_input('Enter address line 1: ')
    from_address['address_line2'] = raw_input('Enter address line 2: ')
    from_address['address_city'] = raw_input('Enter city: ')
    from_address['address_state'] = raw_input('Enter state: ')
    from_address['address_zip'] = raw_input('Enter zip: ')
    from_address['address_country'] = raw_input('Enter country: ')
    message_payload = raw_input('Enter your message to the legislator: ')

    return from_address, message_payload


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
def send_letter(from_address, message_payload):
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
      from_address = from_address,
      file = 'tmpl_5c64c3094c0e11c',
      merge_variables = {
        'message': message_payload
      },
      color = True
    )
    print '\n\nLetter Generation Response:'
    print letter



