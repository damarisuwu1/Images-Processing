import cv2
import time

# Rutas de los archivos
input_image_path = 'Input/original.jpg'
output_pure_python = 'Output/median_filtered_image_pure.jpg'

# Cargar la imagen en escala de grises como lista anidada (Pure Python)
image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE).tolist()

def median_filter_pure_python(image, kernel_size=7):
    """Aplica el filtro de mediana sin usar NumPy."""
    height = len(image)
    width = len(image[0])
    pad = kernel_size // 2

    # Crear una imagen vacía con valores 0 (Pure Python)
    output = [[0] * width for _ in range(height)]

    for i in range(pad, height - pad):
        for j in range(pad, width - pad):
            # Obtener los vecinos manualmente sin NumPy
            neighborhood = []
            for dx in range(-pad, pad + 1):
                for dy in range(-pad, pad + 1):
                    neighborhood.append(image[i + dx][j + dy])

            # Calcular la mediana manualmente sin np.median()
            neighborhood.sort()
            output[i][j] = neighborhood[len(neighborhood) // 2]

    return output

# Medición de tiempo
start_time = time.time()
pure_python_result = median_filter_pure_python(image)
pure_python_time = time.time() - start_time

print(f"Tiempo de ejecución en Python Puro: {pure_python_time:.4f} s")

# Guardar tiempo en archivo
with open("TIMES", "a") as f:
    f.write(f"Python Puro: {pure_python_time:.6f} segundos\n")
