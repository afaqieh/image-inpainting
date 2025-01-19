# **Image Inpainting with Gradient Descent**

This project demonstrates a basic **image inpainting** algorithm using **Gradient Descent** to restore missing or damaged parts of an image. The implementation includes visualization of results, and a modular design for extensibility.

---

## **Table of Contents**
1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)

---

## **Overview**
Image inpainting is the process of reconstructing lost or deteriorated parts of an image to make it visually plausible. This project:
- Creates masks to simulate damaged regions of an image.
- Applies a **Gradient Descent (GD)** algorithm to restore the masked regions.

---

## **Features**
- **Custom Mask Creation**: Remove pixels from the image.
- **Gradient Descent Algorithm**: Smoothly reconstruct the missing regions.
- **Visualization**: Displays side-by-side comparison of original, masked, and inpainted images.

---

## **Installation**
To run the project, ensure you have Python and the required libraries installed.

### **1. Clone the Repository**
```bash
git clone https://github.com/afaqieh/image-inpainting.git
cd image-inpainting
