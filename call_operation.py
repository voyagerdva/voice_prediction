import NeuroNetLibrary as nn
import NeuroNluLibrary as nlu
import NeuroVoiceLibrary as nv

from hello_logic import Hello_logic as HL
from hangup_logic import Hangup_logic as HU
from forward_logic import Forward_logic as FWD
from recommend_logic import Recommend_logic as RCMD


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

def main_choice(r, ent_list):
    if not r:
        nn.log('condition', 'NULL')
        return RCMD.recommend_default(ent_list)

    if r.has_entity('voicemail') and r.entity('voicemail') == 'true':
        nn.log('condition', 'voicemail=true')
        nn.env('result', 'автоответчик')
        nv.hangup()
        return
    
    if r.has_entity('voicemail') and r.entity('voicemail') == 'false':
        nn.log('condition', 'voicemail=false')
        return HL.hello_null(r)

    if r.has_entity('voicemail') and r.entity('repeat') == 'false':
        nn.log('condition', 'repeat=false')
        return HL.hello_repeat(r)


############################################################################


def forward_logic(r):
    pass



