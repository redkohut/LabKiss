from datetime import datetime as dt
from tickets import Ticket, AdvanceTicket, LateTicket, StudentTicket
import json
import os
from event import Event
from datetime import datetime

filename = 'events.json'


def load_events(filenames):
    if not isinstance(filename, str):
        raise TypeError('filename must be of type str')
    if not filenames.endswith('.json'):
        raise ValueError('invalid json file name')
    if os.path.isfile(filenames):
        with open(filenames, 'r') as f:
            return json.load(f, object_hook=decode_event)
    else:
        return list()

def decode_event(dct):
    if 'IT event' in dct:
        return Event(dct['IT event'], dct['id'], datetime.strptime(dct['event date'], '%Y-%m-%d').date(),
                     dct['standard price'])

    return dct


if __name__ == '__main__':
    # events = load_events(filename)
    # print(events)
    ###################################
    # s = open('events.json', 'r')
    # for line in s.readlines():
    #     try:
    #         data = json.loads(line)
    #         print(data)
    #     except ValueError:
    #         # You probably have bad JSON
    #         continue
    event1 = Event('BRECKERS GAME JAM', 1, datetime.strptime('2022-07-15', '%Y-%m-%d').date(), 1000.0)
    print(event1.name)
