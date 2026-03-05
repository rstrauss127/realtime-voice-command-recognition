# Helper function to get input index for specific name
#Get index of microphone name BLue snowball ice
import pyaudio

def list_devices(device_name = ''):
    p = pyaudio.PyAudio()
    device_count = p.get_device_count()
    device_index = -1
    
    for i in range(0, device_count):
        info = p.get_device_info_by_index(i)
        
        # Grab index of device name
        #if info['name'] == device_name:
        #    device_index = i
        
        print(f"Device {info['index']}: {info['name']}")
    p.terminate()
    #print(blue_ice_index)
    return device_index

list_devices()
