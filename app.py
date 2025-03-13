
from flask import Flask, request, render_template, send_file,url_for
from PIL import Image, ImageDraw, ImageFont
import os

app = Flask(__name__)

UPLOAD_FOLDER = "./uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/")
def index():
    return render_template("home_page.html")

@app.route("/upload", methods=["POST"])
def upload():
    # Get the uploaded file and label
    print("In def function")
    image_file = request.files["image"]
    label = request.form["label"]
    
    # Save the uploaded image temporarily
    image_path = os.path.join(UPLOAD_FOLDER, image_file.filename)
    image_file.save(image_path)

    # Open the image and draw the label
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    # Customize your font path if needed
    font = ImageFont.load_default()
    text_position = (300, 50)  # Adjust as needed
    draw.text(text_position, label, fill="red", font=font)

    # Save the labeled image
    labeled_image_path = os.path.join(UPLOAD_FOLDER, "labeled_" + image_file.filename)
    image.save(labeled_image_path)

    # Serve the labeled image back to the user
    return send_file(labeled_image_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
