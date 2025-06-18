Handwritten Digit Recognizer


Explain: What is this project about?
This project, Handwritten Digit Recognizer, is an AI-powered web application that leverages machine learning to identify handwritten digits (0-9) using a Convolutional Neural Network (CNN) trained on the MNIST dataset. The application allows users to upload an image of a handwritten digit, previews it on a simple web interface, and predicts the digit with a confidence score. Built with Python, Flask, Keras, and TensorFlow, it demonstrates end-to-end machine learning development, from model training to deployment.
Why: Why is this project important?
Handwritten digit recognition is a foundational problem in computer vision and machine learning, with applications in postal automation, form processing, and assistive technology for the visually impaired. This project showcases the practical implementation of a CNN, achieving high accuracy on the MNIST dataset, and provides a user-friendly interface to interact with the model. It serves as a learning resource for beginners in AI/ML and a proof-of-concept for deploying machine learning models via web applications, highlighting the potential of AI in real-world digit recognition tasks.

Project Structure

app.py: Flask application to handle image uploads and predictions.
templates/index.html: HTML template for the web interface with image preview.
train_digit_recognizer.ipynb: Jupyter notebook with model training code and testing.
mnist.keras: Trained CNN model file.
digit.png: Sample handwritten digit image.
ipynb_checkpoints/: Notebook checkpoints.
templates/: Folder for HTML templates.
testing images/: Folder for testing images.

What I Have Done and Achieved

Data Preparation: Loaded and preprocessed the MNIST dataset, reshaping and normalizing 60,000 training and 10,000 test samples.
Model Development: Built and trained a CNN with two convolutional layers, max pooling, dropout, and dense layers, achieving 99.20% accuracy on the test set.
Model Deployment: Integrated the trained model into a Flask web app, enabling real-time digit prediction.
User Interface: Designed a simple web interface with image preview, centered layout, and persistent display post-prediction, enhanced with a black border for visual appeal.
Testing: Successfully predicted custom images (e.g., digit.png with 69% confidence for digit 8) and organized testing images in a dedicated folder.
Version Control: Prepared the project for GitHub upload with a structured directory and documentation.

Future Improvements

Add support for multiple image uploads.
Enhance the UI with CSS frameworks (e.g., Bootstrap).
Implement model optimization for faster predictions.



MNIST dataset from Keras.
Inspiration from online AI/ML tutorials and Flask documentation.

