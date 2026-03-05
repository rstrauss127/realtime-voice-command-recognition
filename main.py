import numpy as np
import tensorflow.lite as tflite
from recording_helper import record_audio, terminate
from tf_helper import preprocess_audiobuffer
import os

# Define commands
commands = ['stop', 'yes', 'left', 'no', 'right', 'go', 'up', 'down']

# Create full path to the model file
model_path = os.path.join('realtime-voice-command-recognition', "model_mel_lite.tflite") 

# Load TensorFlow Lite Model
interpreter = tflite.Interpreter(model_path=model_path)
interpreter.allocate_tensors()

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def predict_mic():
    # Record audio and preprocess it into a spectrogram
    audio = record_audio()
    spec = preprocess_audiobuffer(audio)

    # Ensure input tensor is the correct type
    input_data = spec.numpy().astype(np.float32)  # Convert Tensor to numpy and cast

    # Set the input tensor for the model
    interpreter.set_tensor(input_details[0]['index'], input_data)

    # Run the inference
    interpreter.invoke()

    # Get the model's output
    prediction = interpreter.get_tensor(output_details[0]['index'])

    # Determine the command with the highest probability
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
