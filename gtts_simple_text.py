from gtts import gTTS
import os

print('\n\nHello, welcome to our simple test of gtts!\n\n')

meses = int(input('Months that you spend coding by year: '))

if meses < 2:
    meuTexto = 'You have to work harder!'
else:
    meuTexto = 'Ok, you are doing a good job, but go to pub sometimes, buddy!'

language = 'en'

saida  = gTTS(text=meuTexto, lang=language, slow=False)

saida.save('audio_test.mp3')

os.system('start audio_test.mp3')