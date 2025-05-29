# CNN-Image-Colorization-Structural-Analysis
# Deep Image Colorization for Structural Analysis of Aluminum Microstructures

This project introduces a novel deep learning framework that uses image colorization via convolutional neural networks (CNNs) to predict the strain field components of aluminum microstructures. It offers a faster and comparably accurate alternative to traditional Finite Element Analysis (FEA) tools for microstructural materials modeling.

---

## 📌 Description

Structural analysis is a critical step in the engineering design process, enabling engineers to predict how materials and components will perform under various loading conditions. At the microstructural level, such analysis becomes even more important, as the internal structure of materials like aluminum can significantly influence their macroscopic mechanical properties. 

Traditional tools such as CAD and Finite Element Analysis (FEA) software, while powerful, are often computationally expensive and time-consuming—especially when applied to complex microstructures—ultimately slowing down the iterative design and innovation cycle. 

This project presents a deep neural network (DNN)-based approach that leverages convolutional neural networks (CNNs) for image colorization of aluminum microstructures. By doing so, it aims to accelerate the simulation and analysis process without compromising accuracy, offering a more efficient alternative to conventional FEA methods in microstructural material modeling.

---

## Setting and Hypothesis
This approach treats a microstructure containing porosity defects as a grayscale input image and uses image colorization techniques to predict the three strain field components—∊xx,∊yy, and ∊xy —which are represented as the red, green, and blue (RGB) output channels, respectively, as shown in the following figure 
(Image taken from https://doi.org/10.1016/j.commatsci.2020.110068).

<img width="424" alt="image" src="https://github.com/user-attachments/assets/ca914f99-58c6-46ff-8f7e-ca1a10a2a6a8" />


---
## 🧠 Methodology

- **Input**: Grayscale images of aluminum microstructures with porosity defects.
- **Output**: RGB colorized images where each channel represents a strain field component.
- **Technique**: CNN-based image colorization using `.mat` datasets generated via Abaqus simulations.

### 🔧 Programming Languages & Tools

- Python
- MATLAB
- Abaqus API

### 📚 Libraries Used

- TensorFlow
- Keras
- NumPy
- SciPy
- Matplotlib
- Pandas

---

## 📂 Dataset Overview

All datasets used for training and testing are stored in `.mat` format and can be accessed [here](https://doi.org/10.1016/j.dib.2020.106627).

### Dataset Types:

- **Training CNN and Prediction Time Comparison** – 1000 samples with circular defects.
- **Experimental Analysis** – 10 samples per experiment set.
- **Feature Learning** – 500 training and 50 testing samples for 6 unique defect shapes.

### Material Specs:

- **Material**: Aluminum (Al6061-T6)
- **Standards**: ASTM E8/E8M
- **Dimensions**: 38.1 mm × 6 mm
- **Strain field size**: 636 × 101 pixels
- **Defect shapes**: Circular, Elliptical, Rectangular, Triangular, Crescent, Peanut
- **Defect area fraction**: 7–9%
- **FEA conditions**: Uniaxial displacement (0.1 mm), plane-strain mode

The main data consists of 1000 samples of microstructures with 100 circular porosity defects having their radii uniformly distributed in the range 0.1 – 0.5 mm, and their corresponding strain fields.  Additionally, 500 training samples and 50 testing samples of each of microstructures with defect shapes were synthesized. All the data samples are stored in “.mat” file which is used in the image colorization code. The process of generating the datasets for CNN training is as follows:
1.	Use Abaqus API to automate generation of microstructure designs and corresponding strain field results.
2.	Once the data is generated, use the MATLAB code to consolidate the input and output images into a single “.mat” file for the image colorization-based CNN training and testing.

The “.mat” files for all the datasets used in this project can be found here (https://doi.org/10.1016/j.dib.2020.106627):

1.	Training CNN and Prediction Time Comparison - This data contains image data of 1000 samples of microstructures with 100 circular porosity defects having their radii uniformly distributed in the range 0.1 – 0.5 mm, and their corresponding strain fields.  
2.	Experimental Analysis - This data contains image data of two sets of 10 microstructures with circular porosity defects and their strain fields, for each of the two experiments described in the research article.
3.	Feature Learning - This dataset contains six sub-folders each having two datasets (500 samples and 50 samples) of microstructures with porosity defects of six unique shapes described in the aforementioned research article along with their strain fields

## CNN Model Architecture
Reference: https://doi.org/10.1016/j.commatsci.2020.110068
<img width="398" alt="image" src="https://github.com/user-attachments/assets/55aa1848-db10-4a44-babb-a1926a177d78" />

---

## 🧪 Results

| Metric | CNN | FEA |
|--------|-----|-----|
| **Accuracy (R² value)** | 95.77% | — |
| **Prediction Time** | 0.13 ± 0.0171 sec | 2.23 ± 0.0433 sec |

<img width="463" alt="image" src="https://github.com/user-attachments/assets/2abd514b-9bb5-40bf-86e6-1535cee53df4" />

<img width="295" alt="image" src="https://github.com/user-attachments/assets/180af9d1-4879-4e36-a110-40ca91c0d461" />

The overall results indicate the deep neural networks can successfully replicate the FEA structural analysis considerably faster than the traditional computationally-intensive software FEA software with significant accuracy.

---

## 📈 Publications

- **Journal Paper**: [Computational Materials Science](https://doi.org/10.1016/j.commatsci.2020.110068)
- **Conference Proceedings**: [Procedia Manufacturing](https://doi.org/10.1016/j.promfg.2020.05.138)
- **Dataset**: [Data in Brief](https://doi.org/10.1016/j.dib.2020.106627)

---
