import pvporcupine
import pyaudio
import numpy as np
def test_wake_word(model_path, access_key):
    # Initialize Porcupine with your custom wake word model
    porcupine = pvporcupine.create(
        access_key=access_key,
        keyword_paths=[model_path]
    )

    # Initialize PyAudio
    pa = pyaudio.PyAudio()
    stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length,
    )
    stream.start_stream()

    print("Listening for wake word...")
    try:
        while True:
            pcm = stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = np.frombuffer(pcm, dtype=np.int16)
            keyword_index = porcupine.process(pcm)
            if keyword_index >= 0:
                print("Wake word detected!")
                break
    except KeyboardInterrupt:
        print("Stopping...")
    finally:
        stream.stop_stream()
        stream.close()
        pa.terminate()
        porcupine.delete()

# Replace with the path to your .ppn file and your Picovoice access key
model_path = "./model.ppn"
access_key = "nMsi/klZiMGxXZv3pYK6VEYJw3LpaF61XvNzF7nE4WnYQ2F9LbDUeQ=="

test_wake_word(model_path, access_key)

