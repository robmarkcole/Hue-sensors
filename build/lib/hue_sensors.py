"""
Standalone code for parsing API data.
"""
import logging


_LOGGER = logging.getLogger(__name__)
TAP_BUTTON_NAMES = {34: '1_click', 16: '2_click', 17: '3_click', 18: '4_click'}


def parse_hue_api_response(response):
    """Take in the Hue API json response."""
    data_dict = {}    # The list of sensors, referenced by their hue_id.

    # Loop over all keys (1,2 etc) to identify sensors and get data.
    for key in response.keys():
        sensor = response[key]

        if sensor['modelid'] in ['RWL021', 'SML001', 'ZGPSWITCH']:
            _key = sensor['uniqueid'].split(':')[-1][0:5]

            if sensor['modelid'] == 'RWL021':
                data_dict[_key] = parse_rwl(sensor)
            elif sensor['modelid'] == 'ZGPSWITCH':
                data_dict[_key] = parse_zpg(sensor)
            else:
                if _key not in data_dict.keys():
                    data_dict[_key] = parse_sml(sensor)
                else:
                    data_dict[_key].update(parse_sml(sensor))

        elif sensor['modelid'] == 'HA_GEOFENCE':
            data_dict['Geofence'] = parse_geofence(sensor)
    return data_dict


def parse_sml(response):
    """Parse the json for a SML001 Hue motion sensor and return the data."""
    if 'ambient light' in response['name']:
        data = {'light_level': response['state']['lightlevel']}

    elif 'temperature' in response['name']:
        data = {'temperature': response['state']['temperature']/100.0}

    else:
        name_raw = response['name']
        arr = name_raw.split()
        arr.insert(-1, 'motion')
        name = ' '.join(arr)
        hue_state = response['state']['presence']
        if hue_state is True:
            state = 'on'
        else:
            state = 'off'

        data = {'model': response['modelid'],
                'state': state,
                'name': name}
    return data


def parse_zpg(response):
    """Parse the json response for a ZGPSWITCH Hue Tap."""
    press = response['state']['buttonevent']

    button = TAP_BUTTON_NAMES[press]

    data = {'model': 'ZGPSWITCH',
            'name': response['name'],
            'state': button,
            'last_updated': response['state']['lastupdated'].split('T')}
    return data


def parse_rwl(response):
    """Parse the json response for a RWL021 Hue remote."""
    press = str(response['state']['buttonevent'])

    if press[-1] in ['0', '2']:
        button = str(press)[0] + '_click'
    else:
        button = str(press)[0] + '_hold'

    data = {'model': 'RWL021',
            'name': response['name'],
            'state': button,
            'last_updated': response['state']['lastupdated'].split('T')}
    return data


def parse_geofence(response):
    """Parse the json response for a GEOFENCE and return the data."""
    hue_state = response['state']['presence']
    if hue_state is True:
        state = 'on'
    else:
        state = 'off'
    data = {'name': response['name'],
            'model': 'Geofence',
            'state': state}
    return data
