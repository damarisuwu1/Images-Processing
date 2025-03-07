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
## Running the Gaussian Filter
To apply the Gaussian Filter with different implementations, run:

### Execution

### 1. Pure Python Implementation  

Run the following command:  
```bash
python Scripts/pure_python.py
```  

### 2. NumPy Implementation  

Run:  
```bash
python Scripts/only_numpy.py
```  

### 3. Cython + NumPy Implementation  

``` bash
python __main__.py
```
This will:

   - **Load images from Files/Input/.**
   - **Apply the Gaussian filter using Pure Python, NumPy, and Cython implementations.**
   - **Save the processed images in Files/Output/.**
   - **Log execution time in the terminal.**

## Project Structure
```bash
image-processing-filters/
│── gaussian/
│   │── Files/
│   │   │── Input/                 # Folder containing the original images
│   │   │── Output/                # Processed images stored here
│   │── Scripts/
│   │   │── pure_python.py         # Pure Python implementation of the Gaussian Filter
│   │   │── only_numpy.py          # NumPy implementation of the Gaussian Filter
│   │   │── Cython/
│   │   │   │── numpy_cython.pyx   # Cython implementation of the Gaussian Filter
│   │── __main__.py                # Runs Gaussian Filter using all implementations
│   │── setup.py                   # Script to compile Cython modules
│   │── Resultados.ipynb           # Jupyter Notebook for performance analysis
```
## Performance Analysis
Execution times can be analyzed using the Jupyter notebook (Resultados.ipynb) or by running:
```bash
python __main__.py
```

---

## Usage Instructions
## Running the Median Filter
To apply the Median Filter with different implementations, run:

### Execution  

### 1. Pure Python Implementation  

Run the following command:  
```bash
python pure_python.py
```  

### 2. NumPy Implementation  

Run:  
```bash
python numpy_median.py
```  

### 3. Cython + NumPy Implementation  

First, you need to compile the C files generated by Cython. Run:  
```bash
python setup.py build_ext --inplace
```  

Wait for the `.c` files to be generated. Once the process is complete, you can execute:  
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
│── pure_python.py        # Pure Python implementation
│── numpy_median.py       #NumPy implementation 
│── setup.py              # Script to compile Cython modules
│── results.ipynb         # Jupyter Notebook for performance analysis
│── TIMES                 # Execution time log
```

## Implementation Details
The **Median Filter** is used to remove noise while preserving edges by replacing each pixel with the median of its neighborhood.

---

## Usage Instructions
### Running the Sobel Filter

This project includes three implementations of the Sobel filter for edge detection in images:  

1. **Pure Python** (`Pure_python.py`)  
2. **Python with NumPy** (`Numpy_sobel.py`)  
3. **Cython + NumPy** (`Numpy+Cython.py`)  

## Requirements  

Before running any script, install the necessary dependencies with:  

```bash
pip install -r requirements.txt
```  

## Execution  

### 1. Pure Python Implementation  

Run the following command:  
```bash
python Pure_python.py
```  

### 2. NumPy Implementation  

Run:  
```bash
python Numpy_sobel.py
```  

### 3. Cython + NumPy Implementation  

First, you need to compile the C files generated by Cython. Run:  
```bash
python setup.py build_ext --inplace
```  

Wait for the `.c` files to be generated. Once the process is complete, you can execute:  
```bash
python Numpy+Cython.py
```

## Intput Files  

 As long as you have a PNG or  a JPG  in the input carpet the code should wpork just fine

## Output Files  

The processed results from each implementation will be stored in the `Output/` folder with descriptive names:  
- `sobel_filtered_image_pure.png`  
- `sobel_filtered_image_numpy.png`  
- `sobel_filtered_image_cython.png`  



## **Notes**
- Ensure that the Input/ folder contains grayscale images before running the filter.
- The Output/ folder stores the processed images after filtering.
- Modify kernel sizes and parameters inside the script to experiment with different filter strengths.
