from main import app
from db import database


@app.get("/api/v1/get_csv_data")
def get_csv():
    return {"message": "Hello World"}


    