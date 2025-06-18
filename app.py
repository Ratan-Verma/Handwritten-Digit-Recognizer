from flask import Flask, request, render_template
from PIL import Image
import numpy as np
from keras.models import load_model

app = Flask(__name__)
model = load_model('mnist.keras')

@app.route('/', methods=['GET', 'POST'])
def index():
    result = "Upload a digit image"
    if request.method == 'POST':
        if 'image' not in request.files or not request.files['image'].filename:
            result = "No file selected"
        else:
            file = request.files['image']
            try:
                img = Image.open(file).convert('L').resize((28, 28))
                img_array = np.array(img)
                img_array = np.invert(img_array)  # Match MNIST
                img_array = np.where(img_array > 128, 255, 0)  # Threshold
                img_array = img_array.reshape(1, 28, 28, 1) / 255.0
                prediction = model.predict(img_array)[0]
                digit = np.argmax(prediction)
                confidence = float(np.max(prediction)) * 100
                result = f"Digit: {digit}, Confidence: {confidence:.2f}%"
            except Exception as e:
                result = f"Error: {str(e)}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)