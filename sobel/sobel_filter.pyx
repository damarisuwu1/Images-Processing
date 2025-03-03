import numpy as np
cimport numpy as np
cimport cython
import math

@cython.boundscheck(False)  # Disable bounds checking for performance
@cython.wraparound(False)  # Disable negative index wrapping for performance
def apply_sobel_filter(np.ndarray[float, ndim=2] grayscale_image, int width, int height):
    # Define Sobel filters as NumPy arrays inside the function
    cdef np.ndarray[float, ndim=2] Gx = np.array([[1.0, 0.0, -1.0],
                                                  [2.0, 0.0, -2.0],
                                                  [1.0, 0.0, -1.0]], dtype=np.float32)
    
    cdef np.ndarray[float, ndim=2] Gy = np.array([[1.0, 2.0, 1.0],
                                                  [0.0, 0.0, 0.0],
                                                  [-1.0, -2.0, -1.0]], dtype=np.float32)
    
    # Use numpy function to create the array
    cdef np.ndarray[float, ndim=2] sobel_image = np.zeros((height, width), dtype=np.float32)
    
    cdef int x, y, i, j
    cdef float gx, gy
    
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            gx = 0
            gy = 0
            for i in range(3):
                for j in range(3):
                    gx += Gx[i, j] * grayscale_image[y + i - 1, x + j - 1]
                    gy += Gy[i, j] * grayscale_image[y + i - 1, x + j - 1]
            
            sobel_image[y, x] = math.sqrt(gx**2 + gy**2)
    
    return sobel_image
