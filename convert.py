from pydub import AudioSegment

# Load the original audio
audio = AudioSegment.from_file("ss_audio.wav")

# Convert to mono (if it's not already) and downsample to 16kHz
audio = audio.set_frame_rate(16000).set_channels(1)

# Duplicate the mono channel to create fake stereo
fake_stereo = AudioSegment.from_mono_audiosegments(audio, audio)

# Export the fake stereo audio
fake_stereo.export("converted.wav", format="wav")

