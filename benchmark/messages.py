import sys
import json

from collections import OrderedDict

from protolite import encoder


class decoding(object):
    phone_number = {
        1: {
                "name": "country_code",
                "type": "uint32",
                "scope": "optional"
        },
        2: {
                "name": "number",
                "type": "string",
                "scope": "optional"
        }
}
    us_address = {
        1: {
                "name": "street",
                "type": "string",
                "scope": "optional"
        },
        2: {
                "name": "city",
                "type": "string",
                "scope": "optional"
        },
        3: {
                "name": "state",
                "type": "string",
                "scope": "optional"
        },
        4: {
                "name": "zip_code",
                "type": "string",
                "scope": "optional"
        },
        5: {
                "name": "country",
                "type": "string",
                "scope": "optional"
        }
}
    user = {
        1: {
                "name": "user_id",
                "type": "uint64",
                "scope": "optional"
        },
        2: {
                "name": "first_name",
                "type": "string",
                "scope": "optional"
        },
        3: {
                "name": "last_name",
                "type": "string",
                "scope": "optional"
        },
        4: {
                "name": "user_type",
                "type": "enum",
                "scope": "optional"
        },
        5: {
                "name": "home_address",
                "type": "embedded",
                "scope": "optional"
        },
        6: {
                "name": "phone_numbers",
                "type": "embedded",
                "scope": "repeated"
        }
}


class encoding(object):
    phone_number = {
        "country_code": {
                "type": "uint32",
                "scope": "optional",
                "field": 1
        },
        "number": {
                "type": "string",
                "scope": "optional",
                "field": 2
        }
}
    us_address = {
        "street": {
                "type": "string",
                "scope": "optional",
                "field": 1
        },
        "city": {
                "type": "string",
                "scope": "optional",
                "field": 2
        },
        "state": {
                "type": "string",
                "scope": "optional",
                "field": 3
        },
        "zip_code": {
                "type": "string",
                "scope": "optional",
                "field": 4
        },
        "country": {
                "type": "string",
                "scope": "optional",
                "field": 5
        }
}
    user = {
        "user_id": {
                "type": "uint64",
                "scope": "optional",
                "field": 1
        },
        "first_name": {
                "type": "string",
                "scope": "optional",
                "field": 2
        },
        "last_name": {
                "type": "string",
                "scope": "optional",
                "field": 3
        },
        "user_type": {
                "type": "enum",
                "scope": "optional",
                "field": 4
        },
        "home_address": {
                "type": "embedded",
                "scope": "optional",
                "field": 5
        },
        "phone_numbers": {
                "type": "embedded",
                "scope": "repeated",
                "field": 6
        }
}



class wrapper(object):

    def __init__(self, decoding, encoding):
        self.decoding = decoding
        self.encoding = encoding


    def decode(self, message):
        return encoder.decode(self.decoding, message)


    def encode(self, message):
        return encoder.encode(self.encoding, message)


    def _pprint(self, message, encoding):
        fields = OrderedDict()
        for k,v in message.items():
            if encoding[k]['type'] == 'enum':
                v = encoding[k]['message'][v]
            if encoding[k]['type'] in ['embedded', 'repeated']:
                if isinstance(v, list):
                    v = [
                        self._pprint(_v, encoding[k]['message'])
                        for _v in v
                    ]
                else:
                    v = self._pprint(v, encoding[k]['message'])
            fields[k] = v
        return fields


    def pprint(self, message, encoding=None, stream=sys.stdout):
        if encoding is None:
            encoding = self.encoding
        fields = self._pprint(message, encoding)
        stream.write(json.dumps(fields, indent=8, separators=(',', ': ')))
        stream.write('\n')


phone_number = wrapper(decoding.phone_number, encoding.phone_number)
us_address = wrapper(decoding.us_address, encoding.us_address)
user = wrapper(decoding.user, encoding.user)


user.STANDARD = 0
user.ADMIN = 1


user.user_type = dict()
user.user_type[0] = "STANDARD"
user.user_type[1] = "ADMIN"

decoding.user[5]["message"] = decoding.us_address
decoding.user[6]["message"] = decoding.phone_number

encoding.user["home_address"]["message"] = encoding.us_address
encoding.user["phone_numbers"]["message"] = encoding.phone_number

encoding.user["user_type"]["message"] = user.user_type
