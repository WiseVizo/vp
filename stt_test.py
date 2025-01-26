from vosk import Model, KaldiRecognizer
import wave
import json
import sys
import pyaudio

# Path to the downloaded model folder
MODEL_PATH = "model/vosk-model-small-en-us-0.15"

# Load the Vosk model
model = Model(MODEL_PATH)

# Path to your test audio file
AUDIO_FILE = "output/test.wav"

if sys.argv[1]:
    AUDIO_FILE = sys.argv[1]

# Open the audio file
with wave.open(AUDIO_FILE, "rb") as wf:
    # Ensure audio format is supported
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getframerate() not in [8000, 16000, 32000, 44100]:
        raise ValueError("Audio file must be mono, 16-bit, and a supported sample rate (e.g., 16kHz).")

    # Initialize recognizer
    rec = KaldiRecognizer(model, wf.getframerate())

    print("Transcribing audio...")
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break

        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            print(result["text"])

    # Final partial result
    print("Final Result:", json.loads(rec.FinalResult())["text"])

