
def say_it(thing_to_say):
    print("Saying:",thing_to_say)
    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty("rate",180)  #speed of speech
    #speech voice can be changed, google pyttsx change voice 
    try:
        engine.say(thing_to_say)
        engine.runAndWait()
        return True
    
    except Exception as e:
        print("[---]",e)
        engine.stop()
        return None



