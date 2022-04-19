import speech_recognition as sr
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Adjusting noise.......")
    recognizer.adjust_for_ambient_noise(source, duration=2)
    print("Say Something (Recording for 4 seconds): .......")
    audio_text = recognizer.listen(source,timeout=4)
    
    try:
        print( "Recognizing your speech....... ")
        output_text = recognizer.recognize_google(audio_text,language= "en-AU")
        print("Text: "+output_text)
    except:
        print("Sorry, I did not get that")