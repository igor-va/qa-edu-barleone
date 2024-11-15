FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["pytest", "--driver=Remote", "--host=selenium-hub", "--port=4444", "-v", "-s", "-n auto"]
