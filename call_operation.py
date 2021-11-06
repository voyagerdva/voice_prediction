import NeuroNetLibrary as nn
import NeuroVoiceLibrary as nv

from hello_logic import Hello_logic as HL


def entity_list(some_data):
    ent_list = [some_data]
    return ent_list


def start_call(ent_list):
    r = HL.hello_main(ent_list)
    return hello_choice(r)


def hello_choice(r, ent_list):
    if not r:
        nn.log('condition', 'NULL')
        return HL.hello_null(r, ent_list)

    if r.has_entity('voicemail') and r.entity('voicemail') == 'true':
        nn.log('condition', 'voicemail=true')
        nn.env('result', 'автоответчик')
        nv.hangup()
        return

    if r.has_entity('voicemail') and r.entity('voicemail') == 'false':
        nn.log('condition', 'voicemail=false')
        return HL.hello_null(r)

########################################

some_data = [...]
start_call(some_data)