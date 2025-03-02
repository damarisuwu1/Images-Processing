import time
from PIL import Image
import matplotlib.pyplot as plt
import math
import os

# Rutas de entrada y salida
input_image_path = 'Input/original_image.PNG'
output_image_path = 'Output/sobel_filtered_image_pure.png'

# Marcar el tiempo de inicio
start_time = time.time()

# Cargar la imagen
input_image = Image.open(input_image_path).convert('RGB')  # Convertir a RGB
width, height = input_image.size

# Convertir a escala de grises sin numpy
def to_grayscale(image):
    grayscale = [[0] * width for _ in range(height)]  # Crear matriz vacía
    for y in range(height):
        for x in range(width):
            r, g, b = image.getpixel((x, y))
            gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)  # Fórmula de luminancia
            grayscale[y][x] = gray
    return grayscale

grayscale_image = to_grayscale(input_image)

# Definir filtros Sobel
Gx = [[ 1,  0, -1], 
      [ 2,  0, -2], 
      [ 1,  0, -1]]

Gy = [[ 1,  2,  1], 
      [ 0,  0,  0], 
      [-1, -2, -1]]

# Aplicar el filtro Sobel
def apply_sobel_filter(image):
    sobel_image = [[0] * width for _ in range(height)]
    
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            gx = sum(Gx[i][j] * image[y + i - 1][x + j - 1] for i in range(3) for j in range(3))
            gy = sum(Gy[i][j] * image[y + i - 1][x + j - 1] for i in range(3) for j in range(3))
            
            sobel_image[y][x] = min(255, int(math.sqrt(gx**2 + gy**2)))  # Magnitud del gradiente
    
    return sobel_image

sobel_filtered_image = apply_sobel_filter(grayscale_image)

# Convertir la imagen filtrada en formato PIL para mostrarla y guardarla
filtered_img = Image.new("L", (width, height))  # "L" para imágenes en escala de grises
for y in range(height):
    for x in range(width):
        filtered_img.putpixel((x, y), sobel_filtered_image[y][x])


# Marcar el tiempo de fin
end_time = time.time()
execution_time = end_time - start_time
print(f"Tiempo de ejecución: {execution_time:.4f} segundos")

# Mostrar imágenes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.imshow(input_image)
ax1.set_title("Imagen Original")
ax1.axis("off")

ax2.imshow(filtered_img, cmap="gray")
ax2.set_title("Filtro Sobel")
ax2.axis("off")

plt.show()

# Verificar que la carpeta de salida exista y si no, crearla
os.makedirs(os.path.dirname(output_image_path), exist_ok=True)

# Guardar la imagen filtrada en la carpeta Output
filtered_img.save(output_image_path)


# Calcular el tiempo de ejecución

