# base image
FROM python:3.11-slim

# copy everything present in the current working directory into the app folder present in the base image.
COPY . /app
WORKDIR /app

RUN apt-get update -y && apt-get install -y awscli && rm -rf /var/lib/apt/lists/*

RUN pip install --default-timeout=200 --retries=10 pandas numpy seaborn matplotlib scikit-learn Flask dill
RUN pip install --default-timeout=200 --retries=10 catboost
RUN pip install --default-timeout=200 --retries=10 xgboost-cpu

CMD ["python3", "app.py"]