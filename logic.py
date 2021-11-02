import NeuroNetLibrary as nn
import NeuroNluLibrary as nlu
import NeuroVoiceLibrary as nv

# добавление звонка в очередь на обзвон:
nn.call('89001234567', '25-03-2020 01:00:00', 'mtt', 'second_script', 'sip')

# получение параметров ожидаемого вызова:
gender_env = nn.env('gender')
if gender_env == 'female':
    nn.env('flag', 'vova')
else:
    nn.env('flag', 'default')

lang_env = nn.env('lang')
val_env = (gender_env, lang_env)

# настройка параметров медиа сервера
nv.media_params({'asr': 'google', 'tts': 'yandex'}, val = val_env)


# осуществление вызова и взаимодействие с абонентом:
if nv.has_record('hello', val = val_env):
    nv.say('hello', val = val_env)

# обработка паттернов реакции абонента:
with nv.listen(confirm = 'true') as r:
    if nv.has_record('recommend_main', val = val_env):
        nv.say('recommend_main', val = val_env)

with nv.listen(confirm = 'false') as r:
    if nv.has_record('hangup_wrong_time', val = val_env):
        nv.say('hangup_wrong_time', val = val_env)

with nv.listen(wrong_time='true') as r:
    if nv.has_record('hangup_wrong_time', val = val_env):
        nv.say('hangup_wrong_time', val = val_env)

with nv.listen(repeat='true') as r:
    if nv.has_record('hello_repeat', val = val_env):
        nv.say('hello_repeat', val = val_env)

###
