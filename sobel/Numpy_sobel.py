import time
from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np
import os

# Rutas de entrada y salida
input_image_path = 'Input/original_image.PNG'
output_image_path = 'Output/sobel_filtered_image_numpy.png'

# Marcar el tiempo de inicio
start_time = time.time()

# Cargar la imagen
input_image = imread(input_image_path)

# Obtener dimensiones
[nx, ny, nz] = np.shape(input_image)

# Convertir a escala de grises
gamma = 1.400
r_const, g_const, b_const = 0.2126, 0.7152, 0.0722
r_img, g_img, b_img = input_image[:, :, 0], input_image[:, :, 1], input_image[:, :, 2]
grayscale_image = r_const * r_img ** gamma + g_const * g_img ** gamma + b_const * b_img ** gamma

# Matrices del filtro Sobel
Gx = np.array([[1.0, 0.0, -1.0], [2.0, 0.0, -2.0], [1.0, 0.0, -1.0]])
Gy = np.array([[1.0, 2.0, 1.0], [0.0, 0.0, 0.0], [-1.0, -2.0, -1.0]])
rows, columns = np.shape(grayscale_image)
sobel_filtered_image = np.zeros((rows, columns))

# Aplicar el filtro Sobel
for i in range(rows - 2):
    for j in range(columns - 2):
        gx = np.sum(Gx * grayscale_image[i:i + 3, j:j + 3])
        gy = np.sum(Gy * grayscale_image[i:i + 3, j:j + 3])
        sobel_filtered_image[i + 1, j + 1] = np.sqrt(gx ** 2 + gy ** 2)

# Marcar el tiempo de fin
end_time = time.time()

# Calcular el tiempo de ejecución
execution_time = end_time - start_time
print(f"Tiempo de ejecución: {execution_time:.4f} segundos")

# Mostrar la imagen original y la filtrada
fig2, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.imshow(input_image)
ax1.set_title("Imagen Original")
ax2.imshow(sobel_filtered_image, cmap='gray')
ax2.set_title("Filtro Sobel")

# Mostrar las imágenes
plt.show()

# Verificar que la carpeta de salida exista y si no, crearla
os.makedirs(os.path.dirname(output_image_path), exist_ok=True)

# Guardar la imagen filtrada en la carpeta Output
plt.imsave(output_image_path, sobel_filtered_image, cmap='gray')


