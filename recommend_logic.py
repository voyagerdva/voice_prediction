import NeuroNetLibrary as nn
import NeuroNluLibrary as nlu
import NeuroVoiceLibrary as nv

from hello_logic import Hello_logic as HL
from hangup_logic import Hangup_logic as HU
from forward_logic import Forward_logic as FWD


class Recommend_logic():
    def __init__(self):
        pass

    def recommend_main(self, r):


    def recommend_default(self, ent_list):
        with nv.listen((None, None, 500, 'AND'), entities=ent_list) as r:
            nv.say('recommend_default')

        if r.has_entity('voicemail') and r.entity('repeat') == 'true':
            nn.log('condition', 'repeat=true')
            return self.recommend_repeat(self, r)

        if r.has_entity('voicemail') and r.entity('recommendation') == 'dont_know':
            nn.log('condition', 'recommendation=dont_know')
            return self.recommend_repeat_2(self, r)

        if r.has_entity('voicemail') and r.entity('wrong_time') == 'true':
            nn.log('condition', 'wrong_time=true')
            return HU.hangup_logic(r)

        if r.has_entity('voicemail') and r.entity('question') == 'true':
            nn.log('condition', 'question=true')
            return FWD.forward_logic(r)


    def recommend_repeat(self, r):
        pass


    def recommend_repeat_2(self, r):
        pass

    def recommend_main(self):
        pass


    def recommend_score_negative(self):
        pass


    def recommend_score_neutral(self):
        pass


    def recommend_null(self):
        pass


    def recommend_score_positive(self):
        pass

