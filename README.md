# TinyML-STM32
TMNIST Model Deployment on STM32

This repository demonstrates how to:

1. Train a TensorFlow model on the TMNIST dataset.
2. Quantize the model to TensorFlow Lite.
3. Convert the `.tflite` model into a C array.
4. Deploy the model to an STM32 microcontroller using VS Code (no PlatformIO).

---

## 📁 Folder Structure

project/
├── train_tmnist.py # Trains and saves the model in SavedModel format
├── quantize_tmnist.py # Converts the model to quantized TFLite
├── convert_to_c_array.py # Converts .tflite to C array (.cc file)
├── tmnist_model/ # SavedModel directory
├── tmnist_quant.tflite # Quantized model
├── model_data.cc # TFLite model as a C array
└── README.md

## 1. Train the Model

Install dependencies:

```bash
pip install tensorflow numpy


