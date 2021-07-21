from gtts import gTTS
# pip install gtts
import playsound
# pip install playsound
print("\n\n")
print("Enter (q)uit to quit")
while True: 
    input_text = input("Enter text to speak: ")

    if input_text.lower() == "q" or input_text.lower() == "quit":  
        tts = gTTS("Bye!")
        tts.save('speech.mp3')
        playsound.playsound('speech.mp3', True)
        break
    else:
        tts = gTTS(input_text)
        tts.save('speech.mp3')
        playsound.playsound('speech.mp3', True)
