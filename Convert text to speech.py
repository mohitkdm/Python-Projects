import win32com.client

shoutout=["Mohit"]
speaker = win32com.client.Dispatch("SAPI.SpVoice")

for name in shoutout:
    s=name
    speaker.Speak(f"Hello {name} How are you ")
    speaker.Speak(f"If you fine {name} so take a cup of juice ")
    speaker.Speak(f" Nice to meet you {name}  ")
    