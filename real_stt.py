import pyaudio
from vosk import Model, KaldiRecognizer
import json
import sys

# Path to the Vosk model
MODEL_PATH = "model/vosk-model-small-en-us-0.15"  # Update this path to where your model is

# Initialize Vosk model
model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, 44100)  # Use 16000 Hz for good accuracy

# Initialize PyAudio for microphone input
p = pyaudio.PyAudio()
CHUNK=512

# Open audio stream (make sure to use the correct input device index)
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=44100,
                input=True,
                input_device_index=7,
                frames_per_buffer=CHUNK)

print("Listening...")

while True:
    try:
    # Read audio in chunks
        data = stream.read(CHUNK, exception_on_overflow=False)
    
    # Process audio and recognize speech
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            if "stop" in result['text']:
                print("terminating the stt program")
                break
            # Overwrite previous output with the new result
            sys.stdout.write('\r'+' '*100)
            sys.stdout.write('\r' + "Recognized: " + result['text'])
            sys.stdout.flush()  # Ensure the output is printed immediately
        else:
            # If no full result, print partial result
            continue
            partial_result = json.loads(recognizer.PartialResult())
            sys.stdout.write('\r'+' '*100)
            sys.stdout.write('\r' + "Partial: " + partial_result['partial'])
            sys.stdout.flush()

    except KeyboardInterrupt:
        print("\nTerminating...")
        stream.stop_stream()
        stream.close()
        p.terminate()
