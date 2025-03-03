import cv2
import numpy as np
import time
from scipy.ndimage import median_filter

# Rutas de los archivos
input_image_path = 'Input/original.jpg'
output_numpy = 'Output/median_filtered_image_numpy.jpg'

# Cargar la imagen en escala de grises
image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)

def median_filter_numpy(image, kernel_size=5):
    return median_filter(image, size=kernel_size)

# Medición de tiempo
start_time = time.time()
numpy_result = median_filter_numpy(image)
numpy_time = time.time() - start_time

# Guardar la imagen filtrada
cv2.imwrite(output_numpy, numpy_result)

print(f"Tiempo de ejecución con NumPy: {numpy_time:.4f} s")

with open("TIMES", "a") as f:
    f.write(f"NumPy: {numpy_time:.6f} segundos\n")

