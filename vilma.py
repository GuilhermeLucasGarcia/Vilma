import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import time

audio = sr.Recognizer()
maquina = pyttsx3.init()

def exeComando():
    try:
        with sr.Microphone() as source:
            print("Escutando")
            voz = audio.listen(source)
            time.sleep(1)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'vilma' in comando:
                comando = comando.replace('vilma', '')
                maquina.runAndWait()
    except:
        print("Mic não está ok")
    
    return comando

def vozUsuario():
    comando = exeComando()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime("%H:")
        minutos = datetime.datetime.now().strftime("%M:")
        maquina.say('a Hora atual é de:' + hora + 'horas e' + minutos + 'minutos')
        maquina.runAndWait()
    elif 'ache algo sobre' in comando:
        procurar = comando.replace('ache algo sobre', '')
        wikipedia.set_lang('pt')
        result = wikipedia.summary(procurar,2)
        print(result)
        maquina.say(result)
        maquina.runAndWait()
    elif 'música' in comando:
        musica = comando.replace('música', '')
        result = pywhatkit.playonyt(musica)
        maquina.say('Tocando musica')
        maquina.runAndWait()
vozUsuario()
