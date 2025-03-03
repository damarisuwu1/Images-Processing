import numpy as np
cimport numpy as np
cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
cdef unsigned char quickselect(unsigned char[:] arr, int left, int right, int k):
    """Algoritmo QuickSelect para encontrar la k-ésima menor mediana más rápido."""
    cdef int pivot, i, j, temp
    
    while left < right:
        pivot = arr[right]
        i = left - 1
        for j in range(left, right):
            if arr[j] <= pivot:
                i += 1
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
        temp = arr[i+1]
        arr[i+1] = arr[right]
        arr[right] = temp
        pivot = i + 1

        if k < pivot:
            right = pivot - 1
        elif k > pivot:
            left = pivot + 1
        else:
            return arr[pivot]
    return arr[left]

cpdef np.ndarray[np.uint8_t, ndim=2] median_filter_cython(np.ndarray[np.uint8_t, ndim=2] image, int kernel_size=3):
    """Aplica el filtro de mediana usando QuickSelect para mejor rendimiento."""
    cdef int height = image.shape[0]
    cdef int width = image.shape[1]
    cdef int pad = kernel_size // 2
    cdef np.ndarray[np.uint8_t, ndim=2] output = np.zeros_like(image)
    
    cdef int i, j, dx, dy, x, y, idx
    cdef unsigned char[:] window = np.empty(kernel_size * kernel_size, dtype=np.uint8)
    
    for i in range(pad, height - pad):
        for j in range(pad, width - pad):
            idx = 0
            for dx in range(-pad, pad + 1):
                for dy in range(-pad, pad + 1):
                    x = i + dx
                    y = j + dy
                    window[idx] = image[x, y]
                    idx += 1
            
            output[i, j] = quickselect(window, 0, kernel_size * kernel_size - 1, kernel_size * kernel_size // 2)
    
    return output