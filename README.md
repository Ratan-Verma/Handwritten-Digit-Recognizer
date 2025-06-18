# 🧠 Handwritten Digit Recognizer

## 📌 Overview

### 🧾 eXplain: What is this project about?

This project, **Handwritten Digit Recognizer**, is an AI-powered web application that leverages machine learning to identify handwritten digits (0–9) using a **Convolutional Neural Network (CNN)** trained on the **MNIST** dataset.

The application allows users to:

- Upload an image of a handwritten digit
- Preview it on a simple web interface
- Predict the digit with a confidence score

Built with **Python**, **Flask**, **Keras**, and **TensorFlow**, it demonstrates end-to-end machine learning development — from model training to deployment.

---

### ❓ Why: Why is this project important?

Handwritten digit recognition is a foundational problem in computer vision and machine learning, with applications in:

- **Postal automation**
- **Bank cheque verification**
- **Form digitization**
- **Assistive technology for the visually impaired**

This project:

- Demonstrates a practical CNN implementation
- Achieves high accuracy on the MNIST dataset
- Offers a user-friendly interface to interact with the model
- Serves as a **learning resource** for AI/ML beginners
- Acts as a **proof-of-concept** for deploying ML models via web applications

---

## 🧰 Uses of This Project

This project can be used in:

- 🧪 **Educational Use**: Helps students and beginners understand machine learning model development and deployment.
- 💼 **Prototyping**: Acts as a base for building more complex handwritten recognition systems (e.g., for alphabets or signatures).
- 🔍 **Demo App**: Useful for demonstrating AI capabilities in seminars or interviews.
- 🧾 **Digit Recognition Utility**: Can be extended into real-world systems that read handwritten numeric forms.

---

## ⚙️ Getting Started

### 🔧 Prerequisites

- Python 3.12  
- pip (Python package manager)  
- Git (for version control)

### 📥 Installation

#### Clone the repository:

```bash
git clone https://github.com/your-username/handwritten-digit-recognizer.git
cd handwritten-digit-recognizer
```

#### Install dependencies:

**Create a virtual environment (recommended):**

```bash
python -m venv venv
# On macOS/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate
```

**Install required packages:**

```bash
pip install flask keras tensorflow numpy pillow pywin32
```

#### Verify the model:

Ensure `mnist.keras` is in the project directory (either downloaded or trained as per the notebook).

---

## 🚀 Running the Application

### Start the Flask server:

```bash
python app.py
```

### Access the web interface:

- Open your browser and go to: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
- Upload an image (28x28 px) for best results
- Click **Predict** to view the result and confidence score

---

## 🗂️ Project Structure

```
handwritten-digit-recognizer/
│
├── app.py                    # Flask app handling uploads & predictions
├── mnist.keras               # Trained CNN model file
├── digit.png                 # Sample handwritten digit image
├── train_digit_recognizer.ipynb  # Jupyter notebook for training & testing
├── templates/
│   └── index.html            # HTML web interface
├── testing images/           # Folder for testing images
└── ipynb_checkpoints/        # Notebook auto-checkpoints
```

---

## 🏆 Achievements

### ✅ What I Have Done and Achieved

- **Data Preparation:** Loaded & preprocessed the MNIST dataset (60,000 training, 10,000 test samples)
- **Model Development:** Built and trained a CNN with:
  - 2 convolutional layers
  - Max pooling
  - Dropout
  - Dense layers  
  Achieved **99.20% accuracy** on test set.
- **Model Deployment:** Integrated model into a Flask web app for real-time prediction
- **User Interface:** Created a clean UI with:
  - Image preview
  - Centered layout
  - Persistent post-prediction result
  - Black border for visual appeal
- **Testing:** Predicted custom images like `digit.png` (e.g., 69% confidence for digit 8)
- **Version Control:** Structured project for GitHub upload

---

## 🔮 Future Improvements

- Add support for **multiple image uploads**
- Enhance UI using **CSS frameworks** like Bootstrap
- Optimize model for **faster predictions**

---

## 🙏 Acknowledgments

- **MNIST dataset** from Keras
- Inspiration from online **AI/ML tutorials** and **Flask documentation**

---

## 📄 License

This project is licensed under the **MIT License** — see the `LICENSE` file for details.
