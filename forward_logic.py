import NeuroNetLibrary as nn
import NeuroVoiceLibrary as nv


class Forward_logic():
    def __init__(self):
        pass

    def forward(self):
        nn.log('condition', 'prediction=false')
        nv.say('forward')
        nv.switch_to_the_operator()
