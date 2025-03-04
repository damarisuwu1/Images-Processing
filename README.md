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

## Team Members
- Diego Monroy Minero
- Damaris Yuselin Dzul Uc
- Gerardo Hernandez Widman

## Installation
To run this project, follow these steps:

### 1. **Clone the Repository**
### 2. **Install Dependencies**
### 3. **Compile Cython Modules**
For optimized performance, you need to compile the Cython module:

```bash
python setup.py build_ext --inplace
```

## Usage Instructions
### Running the Median Filter
To apply the Median Filter with different implementations, run:
```bash
python numpy_cython.py
```
This will:

- **Load an image from Input/original.jpg.**
- **Apply the median filter using the Cython implementation.**
- **Save the output in Output/median_filtered_image_cython.jpg.**
- **Log execution time in the TIMES file.**

## Project Structure
```bash
image-processing-filters/
│── Input/                # Folder containing the original images
│── Output/               # Processed images stored here
│── median_filter.pyx     # Cython implementation of the Median Filter
│── numpy_cython.py       # Runs Median Filter with Cython
│── setup.py              # Script to compile Cython modules
│── TIMES                 # Execution time log
│── README.md             # Project documentation
```

## Implementation Details
The **Median Filter** is used to remove noise while preserving edges by replacing each pixel with the median of its neighborhood.

## **Notes**
- Ensure that the Input/ folder contains grayscale images before running the filter.
- The Output/ folder stores the processed images after filtering.
- Modify kernel sizes and parameters inside the script to experiment with different filter strengths.