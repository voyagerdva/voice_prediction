import NeuroNetLibrary as nn
import NeuroNluLibrary as nlu
import NeuroVoiceLibrary as nv

from hello_logic import Hello_logic as HL
from forward_logic import Forward_logic as FWD
from recommend_logic import Recommend_logic as RCMD


class Hangup_logic():

    def __init__(self):
        pass

    def hangup_null(self, r):
        nn.log('condition', 'prediction=false')
        nv.say('hangup_null')
        nv.hangup()

    def hangup_wrong_time(self, r):
        pass

    def hangup_positive(self):
        pass

    def hangup_negative(self):
        pass

