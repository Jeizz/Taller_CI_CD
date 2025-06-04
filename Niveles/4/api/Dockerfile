# Dockerfile

FROM python:3.10-slim

WORKDIR /app

# Solo copiar requirements y hacer pip install primero (mejor cache)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Ahora sí, copiar el resto
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
