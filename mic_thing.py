
def get_user_speech():
    import speech_recognition as sr

    while True:
        r = sr.Recognizer()
        with sr.Microphone() as sourceinput:
             
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(sourceinput, duration=0.2)
             
            #listens for the user's input
            audio2 = r.listen(sourceinput)
            # Using google to recognize audio
            try:
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                print("Queuing:",MyText)
                return MyText
            except Exception as wwa:
                #cause there was annoying issues
                print("[-]",wwa)


while True:   
    print("Listening for your voice command ...[Speak freely]")
    x = get_user_speech()
    import query_module as qm
    qm.qmod(x)
