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

 ![image](https://github.com/user-attachments/assets/118719f4-d386-47f6-af18-a8173ca131bd)

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

---

## 🧪 Results

| Metric | CNN | FEA |
|--------|-----|-----|
| **Accuracy (R² value)** | 95.77% | — |
| **Prediction Time** | 0.13 ± 0.0171 sec | 2.23 ± 0.0433 sec |

CNNs demonstrate a significant speed advantage while maintaining high accuracy in replicating FEA outputs.

---

## 📈 Publications

- **Journal Paper**: [Computational Materials Science](https://doi.org/10.1016/j.commatsci.2020.110068)
- **Conference Proceedings**: [Procedia Manufacturing](https://doi.org/10.1016/j.promfg.2020.05.138)
- **Dataset**: [Data in Brief](https://doi.org/10.1016/j.dib.2020.106627)

---
