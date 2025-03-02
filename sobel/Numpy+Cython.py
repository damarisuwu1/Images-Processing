import time
import numpy as np
import matplotlib.pyplot as plt
from sobel_filter import apply_sobel_filter  # Importa la función desde el archivo Cython compilado
import os

# Rutas de entrada y salida
input_image_path = 'Input/original_image.png'  # Reemplaza con la ruta de tu imagen
output_image_path = 'Output/sobel_filtered_image_cython.png'

# Marcar el tiempo de inicio
start_time = time.time()

# Cargar una imagen en escala de grises (puedes usar cualquier imagen en formato .png o .jpg)
input_image = plt.imread(input_image_path)

# Convertir a escala de grises si es necesario (solo si la imagen tiene varios canales)
if input_image.ndim == 3:
    r_const, g_const, b_const = 0.2126, 0.7152, 0.0722
    r_img, g_img, b_img = input_image[:, :, 0], input_image[:, :, 1], input_image[:, :, 2]
    grayscale_image = r_const * r_img + g_const * g_img + b_const * b_img
else:
    grayscale_image = input_image  # Ya está en escala de grises

# Aplicar el filtro Sobel
height, width = grayscale_image.shape
sobel_image = apply_sobel_filter(grayscale_image, width, height)

# Marcar el tiempo de fin
end_time = time.time()

# Calcular el tiempo de ejecución
execution_time = end_time - start_time
print(f"Tiempo de ejecución: {execution_time:.4f} segundos")


# Mostrar las imágenes original y filtrada
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.imshow(grayscale_image, cmap='gray')
ax1.set_title("Escala de Grises")
ax2.imshow(sobel_image, cmap='gray')
ax2.set_title("Imagen Filtrada Sobel")
plt.show()

# Verificar que la carpeta de salida exista y si no, crearla
os.makedirs(os.path.dirname(output_image_path), exist_ok=True)

# Guardar la imagen filtrada en la carpeta Output
plt.imsave(output_image_path, sobel_image, cmap='gray')

