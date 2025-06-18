from ipycanvas import Canvas
from IPython.display import display
from ipywidgets import Button, HBox, VBox, Output
from PIL import Image
import numpy as np
from keras.models import load_model
import matplotlib.pyplot as plt

# Load the model
model = load_model('mnist.keras')

# Create canvas and buttons
canvas = Canvas(width=100, height=100)
canvas.fill_style = 'white'
canvas.fill_rect(0, 0, 100, 100)
canvas.stroke_style = 'black'
canvas.line_width = 8  # Bold lines to match MNIST
output = Output()

def predict_digit(img):
    img = img.resize((28, 28))
    img = img.convert('L')
    img_array = np.array(img)
    img_array = np.invert(img_array)  # Match digit.png preprocessing
    img_array = np.where(img_array > 128, 255, 0)  # Binary threshold
    Image.fromarray(img_array).save('canvas_digit.png')
    img_array = img_array.reshape(1, 28, 28, 1)
    img_array = img_array / 255.0
    res = model.predict([img_array])[0]
    with output:
        output.clear_output()
        print("Confidence scores for each digit:")
        for i, prob in enumerate(res):
            print(f"Digit {i}: {prob * 100:.2f}%")
        digit, acc = np.argmax(res), max(res)
        print(f"\nPredicted digit: {digit}, Confidence: {int(acc * 100)}%")
        plt.figure(figsize=(4, 4))
        plt.imshow(img_array.reshape(28, 28), cmap='gray')
        plt.title(f"Processed Image")
        plt.axis('off')
        plt.show()
    return digit, acc

def on_draw(event):
    x, y = event['x'], event['y']
    canvas.stroke_line(event['last_x'], event['last_y'], x, y)

def on_predict(_):
    img_data = canvas.to_pil()
    predict_digit(img_data)

def on_clear(_):
    canvas.fill_style = 'white'
    canvas.fill_rect(0, 0, 100, 100)
    with output:
        output.clear_output()

predict_button = Button(description='Predict')
clear_button = Button(description='Clear')
predict_button.on_click(on_predict)
clear_button.on_click(on_clear)

canvas.on_mouse_down(lambda x, y: canvas.begin_path())
canvas.on_mouse_move(on_draw)
canvas.on_mouse_up(lambda x, y: canvas.close_path())

display(VBox([canvas, HBox([predict_button, clear_button]), output]))