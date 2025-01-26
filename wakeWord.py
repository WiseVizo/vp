import pvporcupine
import pyaudio
import numpy as np
def test_wake_word(model_path, access_key):
    # Initialize Porcupine with your custom wake word model
    porcupine = pvporcupine.create(
        access_key=access_key,
        keyword_paths=[model_path]
    )
    print(porcupine.sample_rate)
    print(porcupine.frame_length)
    
    # Initialize PyAudio
    pa = pyaudio.PyAudio()
    stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        input_device_index=7,
        frames_per_buffer=porcupine.frame_length,
    )
    stream.start_stream()
    print(porcupine.sample_rate)
    print(porcupine.frame_length)

    print("Listening for wake word...")
    try:
        while True:
            pcm = stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = np.frombuffer(pcm, dtype=np.int16)
            print(pcm.shape)
            print(pcm)
            #pcm = pcm.reshape(-1, 2)  # Reshape to split left and right channels
            #pcm = pcm.mean(axis=1).astype(np.int16)
            print(f"Audio level: {np.max(np.abs(pcm))}")
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
model_path = "./model2.ppn"
access_key = "nMsi/klZiMGxXZv3pYK6VEYJw3LpaF61XvNzF7nE4WnYQ2F9LbDUeQ=="

test_wake_word(model_path, access_key)

