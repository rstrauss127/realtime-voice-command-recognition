# Realtime Voice Command Recognition

A real-time voice command recognition system that uses TensorFlow Lite to classify spoken commands and control a turtle graphics visualization.

## Overview

This project recognizes audio commands in real-time using a pre-trained TensorFlow Lite model. The system:
- Records 1-second audio clips from your microphone
- Converts audio to mel-spectrograms for feature extraction
- Runs inference using a lightweight TensorFlow Lite model
- Classifies spoken words into one of 8 commands
- Visualizes commands using Python's turtle graphics

**Supported Commands:** `stop`, `yes`, `left`, `no`, `right`, `go`, `up`, `down`

## How It Works

1. **Audio Recording** (`recording_helper.py`)
   - Records 1-second audio samples at 16kHz sample rate
   - Uses PyAudio to capture microphone input

2. **Audio Preprocessing** (`tf_helper.py`)
   - Converts raw audio waveform to mel-spectrogram using Short-Time Fourier Transform (STFT)
   - Creates a 128-channel mel-scale spectrogram for feature extraction

3. **Inference** (`main.py`)
   - Loads the TensorFlow Lite model
   - Runs inference on the mel-spectrogram
   - Returns the predicted command with highest confidence

4. **Visualization** (`turtle_helper.py`)
   - Controls a turtle graphics object based on recognized commands
   - Moves turtle up/down/left/right or stops based on voice input

## Prerequisites

- Python 3.7+
- A working microphone

## Installation

1. **Clone or download this repository**

2. **Install required dependencies:**
   ```bash
   pip install tensorflow tensorflow-io pyaudio
   ```
   
   > **Note on PyAudio:** This can be tricky to install. For macOS, use Homebrew:
   > ```bash
   > brew install portaudio
   > pip install pyaudio
   > ```

3. **Prepare the model:**
   - The pre-trained model is included as `model_mel_lite.tflite`
   - Alternatively, to train your own model, follow the [TensorFlow Audio Classification Tutorial](https://www.tensorflow.org/tutorials/audio/simple_audio) in Google Colab

## Usage

### Run the voice command recognizer with turtle visualization:
```bash
python main.py
```

The system will:
- Start listening for voice commands
- Display "start recording..." in the terminal
- Recognize the spoken command and print the result
- Move the turtle based on the recognized command
- Continue until you say "stop"

### Alternative: Run predictions without turtle graphics:
```bash
python main_2.py
```

## File Descriptions

| File | Purpose |
|------|---------|
| `main.py` | Main entry point - records audio, runs inference, controls turtle |
| `main_2.py` | Alternative version without turtle graphics |
| `recording_helper.py` | Audio recording utilities using PyAudio |
| `tf_helper.py` | Audio preprocessing (converts waveform to mel-spectrogram) |
| `turtle_helper.py` | Turtle graphics visualization |
| `device_list.py` | Lists available audio devices (for debugging microphone issues) |
| `to_lite.py` | Converts TensorFlow model to TensorFlow Lite format |
| `model_mel_lite.tflite` | Pre-trained TensorFlow Lite model (optimized for inference) |
| `saved_model_mel/` | TensorFlow SavedModel format (original trained model) |

## Troubleshooting

### Microphone not detected
```bash
python device_list.py
```
Check the device list and update the `input_device_index` in `recording_helper.py` if needed.

### Wrong command predictions
Ensure the commands in `main.py` match the order used when training the model. The default order is:
```python
commands = ['stop', 'yes', 'left', 'no', 'right', 'go', 'up', 'down']
```

### TensorFlow/PyAudio import errors
Reinstall the dependencies:
```bash
pip install --upgrade tensorflow tensorflow-io pyaudio
```

## Training Your Own Model

To train a custom model with different commands:

1. Follow the [TensorFlow Audio Classification Tutorial](https://www.tensorflow.org/tutorials/audio/simple_audio) in Google Colab
2. Train the model with your desired commands
3. Download the trained model as a zip file
4. Extract it to a directory named `saved_model`
5. Run `to_lite.py` to convert to TensorFlow Lite format
6. Update the `commands` list in `main.py` to match your training order

## Video Tutorial

Watch the original implementation tutorial here:
[![Realtime Voice Command Recognition](https://img.youtube.com/vi/m-JzldXm9bQ/hqdefault.jpg)](https://youtu.be/m-JzldXm9bQ)

## License

This project is based on the TensorFlow audio classification tutorial.
