import tensorflow as tf

# Convert the model
converter = tf.lite.TFLiteConverter.from_saved_model('saved_model_mel') # path to the SavedModel directory
tflite_model = converter.convert()

# Save the model.
with open('model_mel_lite.tflite', 'wb') as f:
  f.write(tflite_model)