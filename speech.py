import speech_recognition as sr


r = sr.Recognizer()
AUDIO_FILE = "sample_audio_long.wav"   #mp3 files are not supported
#AUDIO_FILE = "sample_audio_long.wav"    #these files are in files-section of Class08 folder, on MS Teams.

with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file

recognised_text= r.recognize_google(audio)

print('the text recognized from the audio seems to be: ')
print( recognised_text)
