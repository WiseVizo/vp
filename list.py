import pyaudio

# Create a PyAudio instance
p = pyaudio.PyAudio()

# List all available audio devices
print("Available audio devices:")
for i in range(p.get_device_count()):
    device_info = p.get_device_info_by_index(i)
    print(f"Index {i}: {device_info['name']} - {device_info['maxInputChannels']} input channels")

# Close PyAudio instance
p.terminate()
