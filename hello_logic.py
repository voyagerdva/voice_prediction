import NeuroNetLibrary as nn
import NeuroVoiceLibrary as nv

from hangup_logic import Hangup_logic as HU
from recommend_logic import Recommend_logic as RCMD


class Hello_logic():
    def __init__(self):
        pass

    def hello_main(self, ent_list):
        nn.env('result', 'сброс на приветствии')
        with nv.listen((None, None, 500, 'AND'), entities=ent_list) as r:
            nv.say('hello_main')
        return r
###############################################################################
        tail_count = nn.counter('tail_count')
        nn.env('result', 'сброс на приветствии')
        with nv.listen((None, None, 500, 'AND'), entities=ent_list) as r:
            tail_count = nn.counter('tail_count', '+')
            nv.say('hello_main')

        if not r and tail_count == 1:

            tail_count = nn.counter('tail_count', '+')
            if not r and tail_count == 2:
                nn.log('condition', 'NULL')
                return HU.hangup_null(ent_list)

            nn.log('condition', 'NULL')
            return self.hello_null(r, ent_list)

    def hello_null(self, r, ent_list):
        if not r:
            nn.log('condition', 'NULL')
            return HU.hangup_null(r, ent_list)

        with nv.listen((None, None, 500, 'AND'), entities=ent_list) as r:
            nv.say('hello_null')

        if r.has_entity('voicemail') and r.entity('confirm') == 'true':
            nn.log('condition', 'confirm=true')
            return RCMD.recommend_main(r)

        if r.has_entity('voicemail') and r.entity('confirm') == 'false':
            nn.log('condition', 'confirm=false')
            return HU.hangup_wrong_time(r)

        if r.has_entity('voicemail') and r.entity('wrong_time') == 'true':
            nn.log('condition', 'wrong_time=true')
            return HU.hangup_wrong_time(r)

        if r.has_entity('voicemail') and r.entity('repeat') == 'true':
            nn.log('condition', 'repeat=true')
            return self.hello_repeat(r)


    def hello_repeat(self, ent_list):

        with nv.listen((None, None, 500, 'AND'), entities=ent_list) as r:
            nn.log('condition', 'confirm=true')
            nv.say('hello_repeat')
        return RCMD.recommend_main(r)


        with nv.listen((None, None, 500, 'AND'), entities=ent_list) as r:
            nv.say('hello_null')

        if r.has_entity('voicemail') and r.entity('confirm') == 'true':
            nn.log('condition', 'confirm=true')
            return RCMD.recommend_main(r)

        if r.has_entity('voicemail') and r.entity('DEFAULT') == 'true':
            nn.log('condition', 'DEFAULT=true')
            return RCMD.recommend_main(r)

        if r.has_entity('voicemail') and r.entity('confirm') == 'false':
            nn.log('condition', 'confirm=false')
            return HU.hangup_wrong_time(r)

        if r.has_entity('voicemail') and r.entity('wrong_time') == 'true':
            nn.log('condition', 'wrong_time=true')
            return HU.hangup_wrong_time(r)

        if r.has_entity('voicemail') and r.entity('repeat') == 'true':
            nn.log('condition', 'repeat=true')
            return self.hello_repeat(r)

