import NeuroNetLibrary as nn
import NeuroNluLibrary as nlu
import NeuroVoiceLibrary as nv

from hello_logic import Hello_logic as HL
from hangup_logic import Hangup_logic as HU
from forward_logic import Forward_logic as FWD


class Recommend_logic():
    def __init__(self):
        pass


    def recommend_main(self, ent_list):
        with nv.listen((None, None, 500, 'AND'), entities=ent_list) as r:
            nv.say('recommend_main')
        return r


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
            return HU.hangup_logic(r)

        if r.has_entity('voicemail') and r.entity('question') == 'true':
            nn.log('condition', 'question=true')
            return FWD.forward_logic(r)

    def recommend_null(self, r):
        if r.has_entity('voicemail') and r.entity('repeat') == 'true':
            nv.say('recommend_null')
            nn.log('condition', 'repeat=true')
            return self.recommend_repeat(r)

    def recommend_repeat(self, r):
        if not r:
            nn.log('condition', 'NULL')
            return self.recommend_default(r)

        with nv.listen((None, None, 500, 'AND'), entities=ent_list) as ans:
            nv.say('recommend_default')

        if ans.has_entity('voicemail') and ans.entity('DEFAULT') == 'true':
            nn.log('condition', 'repeat=true')
            nv.say('recommend_repeat')
            return HU.hangup_null(r)



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

