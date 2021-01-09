def say(a):
    """
    It says the given str using a female voice
    :param a: str
    :return: says using speakers
    """
    import pyttsx3
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    engine.say(a)
    engine.runAndWait()
    return None