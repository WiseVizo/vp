"""PyAudio Example: Play a wave file."""

import wave
import sys

import pyaudio


CHUNK = 2048

if len(sys.argv) < 2:
    print(f'Plays a wave file. Usage: {sys.argv[0]} filename.wav')
    sys.exit(-1)

with wave.open(sys.argv[1], 'rb') as wf:
    # Instantiate PyAudio and initialize PortAudio system resources (1)
    p = pyaudio.PyAudio()

    # Open stream (2)
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    # Play samples from the wave file (3)
    data = wf.readframes(CHUNK)
    while len(data):  # Requires Python 3.8+ for :=
        stream.write(data)
        data = wf.readframes(CHUNK)

    # Close stream (4)
    stream.close()

    # Release PortAudio system resources (5)
    p.terminate()
