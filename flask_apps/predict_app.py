import base64
import numpy as np
import io
import sys

from PIL import Image
from tensorflow.python.keras import backend as K
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.models import load_model
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras.preprocessing.image import img_to_array
from flask import request
from flask import jsonify
from flask import Flask

app = Flask(__name__)

print(" * Loading Keras model...", file=sys.stderr)

model = load_model('two_class_model.h5')
prediction = model.predict(np.zeros((1, 224, 224, 3))).tolist()
print('Successfully made prediction', file=sys.stderr)

@app.route("/predict", methods=["POST"])
def predict():
    message = request.get_json(force=True) # returns dict
    encoded = message['image']
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded))
    img_resized = image.resize((224, 224), Image.LANCZOS)
    img_array = np.expand_dims(np.array(img_resized), axis=0)
    prediction = model.predict(img_array).tolist()
    print('prediction: {}'.format(prediction), file=sys.stderr)

    response = {
        'prediction': {
            'gt': prediction[0][0],
            'pt': prediction[0][1]
        }
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)