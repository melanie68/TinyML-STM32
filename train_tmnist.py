import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Dropout
from tensorflow.keras.optimizers import Adam

# Load TMNIST dataset (assuming you have a CSV file)
# You can find TMNIST datasets online or create your own MNIST-like dataset
def load_tmnist(csv_file):
    data = pd.read_csv(csv_file)
    y = data['label'].values
    x = data.drop('label', axis=1).values
    x = x.reshape(-1, 28, 28, 1)  # Reshape to 28x28x1 images
    x = x / 255.0  # Normalize
    return x, y

x, y = load_tmnist("C:\\Users\\jcuen\\Downloads\\archive (1)\\tmnist.csv") # add the path to your file

# Split data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Create a simple model
model = Sequential([
    Flatten(input_shape=(28, 28, 1)),
    Dense(128, activation='relu'),
    Dropout(0.2),
    Dense(10, activation='softmax')
])

model.compile(optimizer=Adam(),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

# Evaluate
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'Test accuracy: {test_acc}')

# Convert to TFLite (float32)
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the model
with open('tmnist_model.tflite', 'wb') as f:
    f.write(tflite_model)

# Quantize the model (int8 quantization)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
def representative_dataset():
    for i in range(100):
        yield [x_train[i:i+1].astype(np.float32)]
converter.representative_dataset = representative_dataset
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
converter.inference_input_type = tf.int8
converter.inference_output_type = tf.int8

quantized_tflite_model = converter.convert()

with open('tmnist_quantized.tflite', 'wb') as f:
    f.write(quantized_tflite_model)

print("Quantized TFLite model saved!")