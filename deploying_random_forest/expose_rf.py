import pickle
from flask import Flask, request
from flasgger import Swagger  # UI
import numpy as np
import pandas as pd

with open('./rf.pkl', 'rb') as model_file:  # use relative paths here!
    model = pickle.load(model_file)

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/predict')
def predict_iris():
    """Example endpoint returning a prediction of iris
    This is using docstrings for specifications.
    ---
    parameters:
    - name: s_len
      in: query
      type: number
      required: true
    - name: s_width
      in: query
      type: number
      required: true
    - name: p_len
      in: query
      type: number
      required: true
    - name: p_width
      in: query
      type: number
      required: true
    responses:
        200:
            description: "text"
    """
    sepal_length = request.args.get("s_len")
    sepal_width = request.args.get("s_width")
    petal_length = request.args.get("p_len")
    petal_width = request.args.get("p_width")

    prediction = model.predict(np.array([[sepal_length, sepal_width,
                                          petal_length, petal_width]]))
    return str(prediction)

@app.route('/predict_file', methods=["POST"])
def predict_file():
    """Example file endpoint returning a prediction of iris
    This is using docstrings for specifications.
    ---
    parameters:
    - name: input_file
      in: formData
      type: file
      required: true
    responses:
        200:
            description: "text"
    """
    input_data = pd.read_csv(request.files.get("input_file"), header=None) # so that the first line is read too
    prediction = model.predict(input_data)
    return str(list(prediction))


if __name__ == '__main__':
    app.run()

# http://127.0.0.1:5000/predict?s_len=5.7&s_width=5.6&p_len=4.3&p_width=5.3
    
# in postman: http://127.0.0.1:5000/predict_file
# switch method to post, in body, form_data, key="input_file", value choose files

# http://localhost:5000/apidocs/
