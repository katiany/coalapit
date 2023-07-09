import os
from fastapi import FastAPI
from src.api.controller.coalesce import coalesce
from src.api.controller.fetch import fetch_data

from src.api.model.response import Response

app = FastAPI(title="Coalesce API")


@app.get("/healthcheck")
def healthcheck():
    return {"message": "ok"}


@app.get("/member_id={member_id}", response_model=Response)
def get(member_id: int) -> Response:
    external_data = fetch_data(member_id)
    return coalesce(external_data)