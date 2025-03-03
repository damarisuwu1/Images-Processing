import numpy as np
import cv2
import time
import sys
sys.path.append("cython")  # Add the Cython folder to the path
import median_filter  # Import Cython implementation


# File paths
input_image_path = 'Input/original.jpg'
output_cython = 'Output/median_filtered_image_cython.jpg'

# Load the grayscale image
image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)

# Measure execution time
start_time = time.time()
cython_result = median_filter.median_filter_cython(image, 3)  # Apply median filter with 3x3 kernel
cython_time = time.time() - start_time

# Save the filtered image
cv2.imwrite(output_cython, cython_result)

print(f"Execution time with Cython: {cython_time:.4f} s")

# Save execution time to file
with open("TIMES", "a") as f:
    f.write(f"Cython: {cython_time:.6f} seconds\n")