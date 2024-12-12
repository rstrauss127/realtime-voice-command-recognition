import pyaudio
import numpy as np

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
p = pyaudio.PyAudio()

# Helper function to get input index for specific name
#Get index of microphone name BLue snowball ice
#def list_devices():
#    p = pyaudio.PyAudio()
#    device_count = p.get_device_count()
#    blue_ice_index = -1
#
#    for i in range(0, device_count):
#        info = p.get_device_info_by_index(i)
#        if info['name'] == 'Blue Snowball iCE':
#            blue_ice_index = i
#        #print(f"Device {info['index']}: {info['name']}")
#    p.terminate()
#    #print(blue_ice_index)
#    return blue_ice_index

def record_audio():
    stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        input_device_index=2, # list_devices() Hard coding for now, see device_cnt.py for getting index of mic by name
        frames_per_buffer=FRAMES_PER_BUFFER
    )

    print("start recording...")

    frames = []
    seconds = 1
    for i in range(0, int(RATE / FRAMES_PER_BUFFER * seconds)):
        data = stream.read(FRAMES_PER_BUFFER)
        frames.append(data)

    # print("recording stopped")

    stream.stop_stream()
    stream.close()
    
    return np.frombuffer(b''.join(frames), dtype=np.int16)

# Terminate audio stream
def terminate():
    p.terminate()