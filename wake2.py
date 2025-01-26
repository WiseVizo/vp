import pvporcupine
import pyaudio
import numpy as np
import resampy  # For high-quality resampling
import wave
def test_wake_word_with_fake_stereo(model_path, access_key):
    # Initialize Porcupine with your custom wake word model
    porcupine = pvporcupine.create(
        access_key=access_key,
        keyword_paths=[model_path]
    )

    print(f"Porcupine sample rate: {porcupine.sample_rate} Hz")
    print(f"Porcupine frame length: {porcupine.frame_length} samples")

    # Initialize PyAudio
    pa = pyaudio.PyAudio()
    stream = pa.open(
        rate=44100,  # Native microphone sample rate
        channels=1,  # Mono input
        format=pyaudio.paInt16,
        input=True,
        input_device_index=7,
        frames_per_buffer=porcupine.frame_length,
    )
    stream.start_stream()

    print("Listening for wake word...")
    # Open the file in write-binary mode
    with wave.open("verify.wav", "wb") as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(16000)
        try:
            while True:
                # Step 1: Read audio data from the microphone
                pcm = stream.read(706, exception_on_overflow=False)
                pcm = np.frombuffer(pcm, dtype=np.int16)
                print(pcm.shape) 
                # Step 2: Resample from 44.1kHz to 16kHz
                pcm_16k = resampy.resample(pcm, 44100, 16000).astype(np.int16)
                print(pcm_16k)
                print("-----------------------------------------------------------")
                # Step 4: Interleave the left and right channels into a single array
                pcm_stereo_interleaved = np.empty(2 * len(pcm_16k), dtype=np.int16)
                pcm_stereo_interleaved[0::2] = pcm_16k  # Fill left channel (even indices)
                pcm_stereo_interleaved[1::2] = pcm_16k  # Fill right channel (odd indices)
                wf.writeframes(pcm_stereo_interleaved)


                # Step 4: Feed the fake stereo audio to Porcupine
                keyword_index = porcupine.process(pcm_stereo_interleaved)
                if keyword_index >= 0:
                    print("Wake word detected!")
                    break
        except KeyboardInterrupt:
            print("Stopping...")
        finally:
        # Cleanup
            stream.stop_stream()
            stream.close()
            pa.terminate()
            porcupine.delete()

# Replace with the path to your .ppn file and your Picovoice access key
model_path = "./model2.ppn"
access_key = "nMsi/klZiMGxXZv3pYK6VEYJw3LpaF61XvNzF7nE4WnYQ2F9LbDUeQ=="

test_wake_word_with_fake_stereo(model_path, access_key)

