FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY loader /app/loader
COPY visualizer /app/visualizer
COPY data /app/data

ENV DATA_DIR=/app/data
