from datetime import datetime
import io

from flask import Flask, request, jsonify

from PIL import Image
from transformers import ViTImageProcessor, ViTForImageClassification

app = Flask(__name__)

processor = ViTImageProcessor.from_pretrained('.')
vitmodel = ViTForImageClassification.from_pretrained('.')


def process_image(image):
    """
    A function that processes image.
    """
    image = Image.open(io.BytesIO(image))
    inputs = processor(images=image, return_tensors="pt")
    outputs = vitmodel(**inputs)
    logits = outputs.logits
    predicted_class_idx = logits.argmax(-1).item()
    return vitmodel.config.id2label[predicted_class_idx]


@app.route('/predict', methods=['POST'])
def upload_file():
    """
    Route to upload an image and process it.
    """

    start_time = datetime.now()
    file = request.files['file']

    # Process the image
    result = process_image(file.read())
    result_time = (datetime.now() - start_time).total_seconds()

    return jsonify(
        {
            "predictions": result,
            'time': f"{result_time: .2f} seconds"
        }
    )


if __name__ == '__main__':
    app.run()
