import numpy as np

from tensorflow import saved_model

from recording_helper import record_audio, terminate
from tf_helper import preprocess_audiobuffer

commands = ['stop', 'yes', 'left', 'no', 'right', 'go', 'up', 'down']
commands = ['stop', 'yes', 'left', 'no', 'right', 'go', 'up', 'down']

loaded_model = saved_model.load('saved_model_mel')

def predict_mic():
    audio = record_audio()
    spec = preprocess_audiobuffer(audio)
    prediction = loaded_model.serve(spec)
    label_pred = np.argmax(prediction, axis=1)
    command = commands[label_pred[0]]
    print("Predicted label:", command)
    return command

if __name__ == "__main__":
    from turtle_helper import move_turtle
    while True:
        command = predict_mic()
        move_turtle(command)
        if command == "stop":
            terminate()
            break