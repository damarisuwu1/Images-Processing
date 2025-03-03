# Images Processing

## Objective

The goal of this assignment is to implement three common image processing filters (Gaussian Filter, Sobel Filter, and Median Filter) and analyze their performance using different computational approaches:

1. Pure Python (No external optimizations)

2. NumPy (Vectorized operations for optimization)

3. NumPy + Cython (Further optimization using compiled  code)

This project evaluates the trade-off between execution time and image quality for each method.
 
## Features
- **Implmentations of three filters:**
    - **Gaussian Filter**: A low-pass filter that reduces noise in images by averaging neighboring pixels.
    - **Sobel Filter**: An edge detection filter that highlights the gradient of intensity changes in an imag
    - **Median Filter**: A non-linear filter that replaces each pixel with the median value of neighboring pixels
- **Performance Analysis**: Execution time and image quality comparison for each filter implementation
