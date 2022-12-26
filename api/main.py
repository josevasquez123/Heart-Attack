from fastapi import FastAPI
import schemas
import os
import pickle
import pandas as pd
from fastapi.encoders import jsonable_encoder

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/model")
def get_ml_model(model_input: schemas.ModelInput):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    model = pickle.load(open(dir_path+"/models/model.pkl", 'rb'))

    df_feats = pd.DataFrame([jsonable_encoder(model_input)])
    predict = model.predict(df_feats)

    return int(predict[0])