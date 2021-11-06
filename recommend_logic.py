import NeuroNetLibrary as nn
import NeuroVoiceLibrary as nv

from hangup_logic import Hangup_logic as HU
from forward_logic import Forward_logic as FWD
from hello_logic import Hello_logic as HL


class Recommend_logic():
    def __init__(self):
        pass


    def recommend_main(self, ent_list):
        tail_count = nn.counter('tail_count')
        with nv.listen((None, None, 500, 'AND'), entities=ent_list) as r:
            tail_count = nn.counter('tail_count', '+')
            nv.say('recommend_main')

        if not r and tail_count == 1:
            tail_count = nn.counter('tail_count', '+')

            if not r and tail_count == 2:
                nn.log('condition', 'NULL')
                return HU.hangup_null(ent_list)

            nn.log('condition', 'NULL')
            return self.recommend_null(ent_list)


        if r.has_entity('voicemail') and r.entity('voicemail') == 'false':
            nn.log('condition', 'voicemail=false')
            return HL.hello_null(r)

        if r.has_entity('voicemail') and r.entity('repeat') == 'false':
            nn.log('condition', 'repeat=false')
            return HL.hello_repeat(r)

    def recommend_default(self, ent_list):
        with nv.listen((None, None, 500, 'AND'), entities=ent_list) as r:
            nv.say('recommend_default')

        if r.has_entity('voicemail') and r.entity('repeat') == 'true':
            nn.log('condition', 'repeat=true')
            return self.recommend_repeat(r)

        if r.has_entity('voicemail') and r.entity('recommendation') == 'dont_know':
            nn.log('condition', 'recommendation=dont_know')
            return self.recommend_repeat_2(r)

        if r.has_entity('voicemail') and r.entity('wrong_time') == 'true':
            nn.log('condition', 'wrong_time=true')
            return HU.hangup_wrong_time(r)

        if r.has_entity('voicemail') and r.entity('question') == 'true':
            nn.log('condition', 'question=true')
            return FWD.forward(r)

    def recommend_null(self, r):
        if r.has_entity('voicemail') and r.entity('recommendation') == 'positive':
            nv.say('recommend_null')
            nn.log('condition', 'repeat=true')
            return self.recommend_score_positive(r)


    def recommend_repeat(self, ent_list):
        tail_count = nn.counter('tail_count')
        with nv.listen((None, None, 500, 'AND'), entities=ent_list) as r:
            tail_count = nn.counter('tail_count', '+')
            nv.say('recommend_repeat')

        if not r and tail_count == 1:
            tail_count = nn.counter('tail_count', '+')

            if not r and tail_count == 2:
                nn.log('condition', 'NULL')
                return HU.hangup_null(ent_list)

            nn.log('condition', 'NULL')
            return self.recommend_default(ent_list)


    def recommend_repeat_2(self, r):
        if r.has_entity('voicemail') and (r.entity('SCORE') >=0 and r.entity('SCORE') <=8):
            nn.log('condition', 'repeat=true')
            nv.say('recommend_repeat_2')
            return HU.hangup_negative(r)


    def recommend_score_negative(self, r):
        if r.has_entity('voicemail') and (r.entity('SCORE') >=8 and r.entity('SCORE') <=10):
            nn.log('condition', 'repeat=true')
            nv.say('recommend_score_negative')
            return HU.hangup_positive(r)


    def recommend_score_neutral(self, r):
        if r.has_entity('voicemail') and (r.entity('SCORE') == "false"):
            nn.log('condition', 'repeat=true')
            nv.say('recommend_score_neutral')
            return self.recommend_score_negative(r)


    def recommend_score_positive(self):
        if r.has_entity('voicemail') and (r.entity('recomendation') == "neutral"):
            nn.log('condition', 'repeat=true')
            nv.say('recommend_score_positive')
            return self.recommend_score_neutral(r)

