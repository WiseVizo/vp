import wave
obj = wave.open("test.wav", "rb")

print(obj.getparams())

frames = obj.readframes(-1)

print(f"{len(frames)} and {type(frames)} and {type(frames[0])}")

obj.close()


new_obj = wave.open("yt.wav", "wb")
new_obj.setnchannels(1)
new_obj.setframerate(44100)
new_obj.setsampwidth(2)
new_obj.writeframes(frames)
new_obj.close()
