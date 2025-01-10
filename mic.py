import pyaudio

p = pyaudio.PyAudio()
print(p.get_default_host_api_info())
print(p.get_default_input_device_info())
#var = p.is_format_supported(44100, input_device=4, input_channels=None, input_format=pyaudio.paInt16, output_device=8, output_channels=None, output_format=pyaudio.paInt16)
#print(var)
print(pyaudio.get_portaudio_version())
p.terminate()

