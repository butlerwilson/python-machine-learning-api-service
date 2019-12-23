from flask import Flask
from flask import request
from flask import jsonify

import joblib
import numpy as np

MODEL_PATH = "./model/rfc.model"
model = joblib.load(MODEL_PATH)

app = Flask(__name__)


@app.route('/', methods=["POST"])
def predict():
    if not request.json or "feature" not in request.json:
        response = {
            "errno": 1,
            "errmsg": "No feature!!!",
            "label": "Unknown"
        }
    else:
        try:
            feature = request.json["feature"]
            label = model.predict(np.array([feature]))

            response = {
                "errno": 0,
                "errmsg": "predict success.",
                "label": int(label[0])
            }
        except Exception as e:
            response = {
                "errno": 2,
                "errmsg": str(e),
                "label": "Unknown"
            }

    return jsonify(response)


if __name__ == '__main__':
    app.run()
