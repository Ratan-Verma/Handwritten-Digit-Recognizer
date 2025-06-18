Handwritten Digit Recognizer
Overview
Welcome to the Handwritten Digit Recognizer, an AI-powered web application designed to identify handwritten digits (0-9) using a Convolutional Neural Network (CNN) trained on the MNIST dataset. Built with Python, Flask, Keras, and TensorFlow, this project showcases an end-to-end machine learning pipeline from training to deployment.

Table of Contents

Explain: What is this project about?
Why: Why is this project important?
Execute: How to set up and run the project
Project Structure
What I Have Done and Achieved
Future Improvements
Acknowledgments
License


Explain: What is this project about?
This project is a web-based AI application that leverages a CNN trained on the MNIST dataset to recognize handwritten digits. Users can upload an image, preview it on a simple interface, and receive a prediction with a confidence score. The solution integrates:

Machine Learning: CNN model development and training.
Web Development: Flask for the backend and HTML for the frontend.
Deployment: Real-time prediction capability.


Why: Why is this project important?
Handwritten digit recognition is a cornerstone of computer vision and machine learning, with practical applications in:

Postal automation.
Form processing.
Assistive technology for the visually impaired.This project demonstrates a high-accuracy CNN (99.20% on test data) and a user-friendly interface, serving as both a learning tool for AI/ML beginners and a proof-of-concept for deploying ML models in web applications.


Execute: How to set up and run the project
Prerequisites

Python 3.12
pip (package manager)
Git (for version control)

Installation

Clone the repository:git clone https://github.com/your-username/handwritten-digit-recognizer.git
cd handwritten-digit-recognizer


Set up a virtual environment (optional but recommended):python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:pip install flask keras tensorflow numpy pillow pywin32


Verify the model:
Ensure mnist.keras is in the project directory.



Running the Application

Start the Flask server:python app.py


Access the web interface:
Open http://127.0.0.1:5000/ in a browser.
Upload an image (must be 28x28 pixels) and click "Predict" to see the result.




Project Structure

app.py: Flask application for handling image uploads and predictions.
templates/index.html: HTML template with a styled web interface.
train_digit_recognizer.ipynb: Jupyter notebook documenting model training and testing.
mnist.keras: Trained CNN model file.
digit.png: Sample handwritten digit image.
ipynb_checkpoints/: Notebook checkpoints.
templates/: Folder for HTML templates.
testing images/: Folder for testing images.


What I Have Done and Achieved

Data Preparation: Preprocessed the MNIST dataset, normalizing 60,000 training and 10,000 test samples.
Model Development: Trained a CNN with convolutional layers, max pooling, dropout, and dense layers, achieving 99.20% accuracy.
Model Deployment: Integrated the model into a Flask web app for real-time predictions.
User Interface: Designed a centered, persistent preview interface with a black border.
Testing: Predicted custom images (e.g., digit.png with 69% confidence for digit 8).
Version Control: Structured the project for GitHub with documentation.


Future Improvements

Support for multiple image uploads.
Enhance UI with CSS frameworks (e.g., Bootstrap).
Optimize the model for faster predictions.


Acknowledgments

MNIST dataset from Keras.
Inspiration from online AI/ML tutorials and Flask documentation.


License
This project is licensed under the MIT License - see the LICENSE file for details.
