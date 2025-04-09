#
# import speech_recognition as sr
#
#
# def recognize_speech():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening... Please speak something.")
#         recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
#         audio = recognizer.listen(source)
#
#         try:
#             text = recognizer.recognize_google(audio, language="en-US")  # Convert speech to text
#             print("You said:", text)
#         except sr.UnknownValueError:
#             print("Sorry, I could not understand the audio.")
#         except sr.RequestError:
#             print("Google Speech Recognition service is unavailable.")
#
#
# if __name__ == "__main__":
#     recognize_speech()
import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Please speak something.")
        audio = recognizer.listen(source)
        try:
            # Instead of FLAC, use WAV format
            text = recognizer.recognize_google(audio, language="en-US")
            print("You said: ", text)
        except sr.UnknownValueError:
            print("Sorry, could not understand your speech.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

recognize_speech()
