import speech_recognition as sr

# Create a recognizer instance
r = sr.Recognizer()

# Use the microphone as the audio source
with sr.Microphone() as source:
    print("Speak something:")
    audio = r.listen(source)

# Recognize speech using Google Web Speech API
try:
    print("You said: " + r.recognize_google(audio, language='fr-FR'))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
