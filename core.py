import ampalibe
from ampalibe import Messenger
from os import environ as env
from ampalibe.ui import Button
from datetime import date

chat = Messenger()

today = date.today()

today_formated = today.strftime("%Y/%m/%d")

@ampalibe.command('/')
def main(sender_id, cmd, **extends):
    if cmd.lower()=='fanala' or cmd.lower()=="f'anala" :
        chat.send_message(sender_id, "Miarahaba tompoko 😊")
        chat.send_message(sender_id, "Tongasoa eto amin'ny  Fanala - Advantista Analamahitsy, pejy natokana hizaràna ny vaovao sy ny tsara ho fantatra eto amin'ny Fiangonana Advantista Mitandrina ny Andro Fahafito Analamahitsy, ary natao indrindra hanampy anao amin'ny fianarana ny Soratra Masina.")
        fandaharanaFototra(sender_id)
        fandaharanaAnkizy(sender_id)
        fandaharanaTanora(sender_id)
        fandaharanaLehibe(sender_id)

def hanohyHijery(sender_id,**extends):
    chat.send_message(sender_id,"Ny Fiangonana Advantista Mitandrina ny Andro Fahafito eto Analamahitsy dia mankasitraka anao amin'ny fahaliananao mandinika ny Tenin'Andriamanitra; ialàna tsiny raha sendra ny tsy fisian'ny fandaharana indraindray noho ny antony izay tsy miankina aminay.")
    buttons = [
        Button(
            type='postback',
            title='Eny',
            payload='/hanohy-hijery-eny'
        ),
        Button(
            type='postback',
            title='Tsia',
            payload='/hanohy-hijery-tsia'
        )
    ]

    return chat.send_button(sender_id, buttons, "Mbola hanohy hijery ireo fandaharana hafa atolotro ve ianao ?")

@ampalibe.command('/hanohy-hijery-eny')
def hanohyHijeryEny(sender_id,**extends):
    fandaharanaFototra(sender_id)
    fandaharanaAnkizy(sender_id)
    fandaharanaTanora(sender_id)
    fandaharanaLehibe(sender_id)

@ampalibe.command('/hanohy-hijery-tsia')
def hanohyHijeryTsia(sender_id,**extends):
    return chat.send_message(sender_id, "Mankasitraka anao ny amin'ny fahaliananao mandinika ny Soratra Masina. Manantena ny mbola hiaraka aminao indray rahampitso. Mbola azonao atao koa ny mikaroka ireo fandaharana hafa atolotro. Mbola maro ihany koa ireo fandaharana hovokarina manokana ho anao.\n\nHomban'i Jesosy manokana anie ianao 😊")

def fandaharanaFototra(sender_id,**extends):
    buttons = [
        Button(
            type='postback',
            title='Mofon\'aina',
            payload='/mofo'
        ),
        Button(
            type='postback',
            title='Source de vie',
            payload='/source-de-vie'
        ),
        Button(
            type='postback',
            title='Araho ny Baiboly',
            payload='/araho-ny-baiboly'
        )
    ]

    return chat.send_button(sender_id, buttons, "Safidio amin'ireto manaraka ireto izay tianao hatolotro ho anao.\n\nFandaharana fototra :")

def fandaharanaAnkizy(sender_id,**extends):
    buttons = [
        Button(
            type='postback',
            title='Lesona Ankizy',
            payload='/lesona-ankizy'
        )
    ]

    return chat.send_button(sender_id, buttons, "Ankizy :")

def fandaharanaTanora(sender_id,**extends):
    buttons = [
        Button(
            type='postback',
            title='Lesona TZ,MTN,ZTV',
            payload='/lesona-tanora-zandriny'
        ),
        Button(
            type='postback',
            title='Lesona Tanora Zokiny',
            payload='/lesona-tanora-zokiny'
        )
    ]

    return chat.send_button(sender_id, buttons, "Tanora :")

def fandaharanaLehibe(sender_id,**extends):
    buttons = [
        Button(
            type='postback',
            title='Lesona Lehibe',
            payload='/lesona-lehibe'
        )
    ]

    return chat.send_button(sender_id, buttons, "Lehibe :")

@ampalibe.command('/mofo')
def mofo(sender_id, cmd, **extends):
    chat.send_message(sender_id, "Indro ary nomeko anao ny mofon'aina natao ho fiambenana maraina anio.")
    chat.send_message(sender_id, "Mahandrasa kely azafady...")
    chat.send_file_url(sender_id, env.get('OASIS_RADIO_API_URL')+today_formated+'/mofo.mp3', filetype='audio')
    hanohyHijery(sender_id)

@ampalibe.command('/source-de-vie')
def mofo(sender_id, cmd, **extends):
    chat.send_message(sender_id, "Indro ary nomeko anao ny mofon'aina amin'ny fiteny frantsay natao ho fiambenana maraina anio.")
    chat.send_message(sender_id, "Mahandrasa kely azafady...")
    chat.send_file_url(sender_id, env.get('OASIS_RADIO_API_URL')+today_formated+'/source.mp3', filetype='audio')
    hanohyHijery(sender_id)

@ampalibe.command('/araho-ny-baiboly')
def mofo(sender_id, cmd, **extends):
    chat.send_message(sender_id, "Indro ary nomeko anao ny \"Araho ny Baiboly\" anio.")
    chat.send_message(sender_id, "Mahandrasa kely azafady...")
    chat.send_file_url(sender_id, env.get('OASIS_RADIO_API_URL')+today_formated+'/baiboly.mp3', filetype='audio')
    hanohyHijery(sender_id)

@ampalibe.command('/lesona-ankizy')
def mofo(sender_id, cmd, **extends):
    chat.send_message(sender_id, "Indro ary omeko anao ny Lesona Sekoly Sabata ho an'ny Ankizy anio.")
    chat.send_message(sender_id, "Mahandrasa kely azafady...")
    chat.send_file_url(sender_id, env.get('OASIS_RADIO_API_URL')+today_formated+'/tda.mp3', filetype='audio')
    hanohyHijery(sender_id)

@ampalibe.command('/lesona-tanora-zandriny')
def mofo(sender_id, cmd, **extends):
    chat.send_message(sender_id, "Indro ary omeko anao ny Lesona Sekoly Sabata ho an'ny Tanora Zandriny, Matoanto, ary Zatovo anio.")
    chat.send_message(sender_id, "Mahandrasa kely azafady...")
    chat.send_file_url(sender_id, env.get('OASIS_RADIO_API_URL')+today_formated+'/tdt.mp3', filetype='audio')
    hanohyHijery(sender_id)

@ampalibe.command('/lesona-tanora-zokiny')
def mofo(sender_id, cmd, **extends):
    chat.send_message(sender_id, "Indro ary omeko anao ny Lesona Sekoly Sabata ho an'ny Tanora Zokiny anio.")
    chat.send_message(sender_id, "Mahandrasa kely azafady...")
    chat.send_file_url(sender_id, env.get('OASIS_RADIO_API_URL')+today_formated+'/ttz.mp3', filetype='audio')
    hanohyHijery(sender_id)

@ampalibe.command('/lesona-lehibe')
def mofo(sender_id, cmd, **extends):
    chat.send_message(sender_id, "Indro ary omeko anao ny Lesona Sekoly Sabata ho an'ny Lehibe anio.")
    chat.send_message(sender_id, "Mahandrasa kely azafady...")
    chat.send_file_url(sender_id, env.get('OASIS_RADIO_API_URL')+today_formated+'/tdl.mp3', filetype='audio')
    hanohyHijery(sender_id)