from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from starlette.config import Config
import uvicorn
import os
from fastai import *
from fastai.vision import *
import urllib

app = Starlette(debug=True)

app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_headers=['*'], allow_methods=['*'])

### EDIT CODE BELOW ###

answer_question_1 = """
Underfitting is when our model has a high bias and does not fit our data very well. For example, if the data looks more like a curve, but the model is a straight line, this is underfitting.  We can tell by checking our data against the validation data set. If the loss is really bad on this set, we've got underfitting.

Overfitting is when our model ha sa high variance. In otherwords it is too tightly coupled to our data and is not generalized. This happens when you run too many epocs during training and you can tell you're overfitting if your error rate improves for a while and then gets worse again.
"""

answer_question_2 = """
Gradient decent is an iterative process that aims to find the local minimum of a function. We accomplish this by moving in the direction of the steepest decent (or negative of the gradient). Gradient decent is used to update the parameters of our model.
"""

answer_question_3 = """
The goal of regression is to help understand how the dependent variable changes when any one of the independent variables is varied. One example of regression analysis is Mean Squared Error, which is a loss which is the difference between some predicitons that you make (your model) and the actual value.
"""

## Replace none with your model
pred_model = 'export.pkl'

@app.route("/api/answers_to_hw", methods=["GET"])
async def answers_to_hw(request):
    return JSONResponse([answer_question_1, answer_question_2, answer_question_3])

@app.route("/api/class_list", methods=["GET"])
async def class_list(request):
    return JSONResponse([ "Replace this array with a list of your classes extracted from your model" ])

@app.route("/api/classify", methods=["POST"])
async def classify_url(request):
    body = await request.json()
    url_to_predict = body["url"]

    ## Make your prediction and store it in the preds variable
    bytes = await get_bytes(request.query_params[url_to_predict])
    img = open_image(BytesIO(bytes))
    _,_,losses = learner.predict(img)

    return JSONResponse({
        "predictions": preds,
    })

### EDIT CODE ABOVE ###

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=int(os.environ['PORT']))
