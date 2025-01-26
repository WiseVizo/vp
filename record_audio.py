import wave
import pyaudio
import sys

# Parameters for recording
FORMAT = pyaudio.paInt16  # 16-bit resolution
CHANNELS = 1  # Mono audio
RATE = 44100  # Use 16000 for DMIC16kHz
CHUNK = 512  # Chunk size
if sys.argv[1]:
    RECORD_SECONDS = int(sys.argv[1]) # Duration of recording
else:
    RECORD_SECONDS = 10
OUTPUT_FILENAME = "output/test.wav"  # Output file name

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open a stream for recording
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                input=True,
                rate=RATE,
                input_device_index=7,# Use 4 for DMIC or 5 for DMIC16kHz
                frames_per_buffer=CHUNK)

print("Recording...")

frames = []  # Store audio frames

# Capture audio data in chunks
for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK, exception_on_overflow=False)
    frames.append(data)

print("Recording complete.")
print(len(frames))
# Stop and close the stream
stream.stop_stream()
stream.close()

# Terminate PyAudio
p.terminate()

# Save the recorded data to a .wav file
with wave.open(OUTPUT_FILENAME, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))

print(f"Audio recorded and saved to {OUTPUT_FILENAME}")

