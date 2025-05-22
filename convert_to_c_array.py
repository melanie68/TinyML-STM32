# convert_to_c_array.py
import numpy as np

def convert_to_c_array(file_path, var_name):
    with open(file_path, 'rb') as f:
        data = f.read()

    hex_array = ', '.join(f'0x{byte:02x}' for byte in data)
    lines = [hex_array[i:i+100] for i in range(0, len(hex_array), 100)]

    with open("model_data.cc", 'w') as f:
        f.write(f'#include <cstdint>\n\n')
        f.write(f'const unsigned char {var_name}[] = {{\n')
        for line in lines:
            f.write(f'  {line},\n')
        f.write('};\n')
        f.write(f'const int {var_name}_len = {len(data)};\n')

convert_to_c_array("tmnist_quant.tflite", "tmnist_quant_tflite")
