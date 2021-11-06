import NeuroNetLibrary as nn
import NeuroVoiceLibrary as nv


class Hangup_logic():

    def __init__(self):
        pass

    def hangup_null(self, r):
        nn.log('condition', 'prediction=false')
        nv.say('hangup_null')
        nv.hangup()

    def hangup_wrong_time(self):
        nn.log('condition', 'prediction=false')
        nv.say('hangup_wrong_time')
        nv.hangup()

    def hangup_positive(self):
        nn.log('condition', 'prediction=false')
        nv.say('hangup_positive')
        nv.hangup()

    def hangup_negative(self):
        nn.log('condition', 'prediction=false')
        nv.say('hangup_negative')
        nv.hangup()