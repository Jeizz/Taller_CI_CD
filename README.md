# Taller: CI/CD y GitOps para Despliegue de API de IA

## 🎯 Objetivo

Diseñar e implementar una arquitectura CI/CD con GitOps para desplegar una API en FastAPI que incluye un modelo de IA, observabilidad con Prometheus y Grafana, y despliegue automatizado usando Docker, GitHub Actions, Kubernetes y Argo CD.

---

## 🧱 Estructura del Proyecto

```
TALLER_CI_CD/
├── .github/workflows/ci-cd.yml
├── Niveles/
│   └── 4/
│       ├── api/
│       │   ├── app/main.py
│       │   ├── app/model.pkl
│       │   ├── train_model.py
│       │   ├── Dockerfile
│       │   └── requirements.txt
│       ├── loadtester/
│       │   ├── main.py
│       │   ├── Dockerfile
│       │   └── requirements.txt
│       ├── manifests/
│       │   ├── api-deployment.yaml
│       │   ├── script-deployment.yaml
│       │   ├── prometheus-deployment.yaml
│       │   ├── grafana-deployment.yaml
│       │   ├── grafana-config/datasources.yaml
│       │   ├── prometheus.yml
│       │   └── kustomization.yaml
│       └── argo-cd/app.yaml
```

---

## 🔄 Flujo CI/CD + GitOps

1. Entrenamiento del modelo con `train_model.py`
2. Construcción y publicación de imágenes Docker para API y LoadTester
3. Sincronización automática de manifiestos YAML con Argo CD
4. Exposición de métricas desde la API y visualización con Grafana

---

## 🔧 Componentes del Proyecto

### 🔹 API (FastAPI)
- Endpoint `/predict`: Predice usando `model.pkl`
- Endpoint `/metrics`: Expone métricas Prometheus

### 🔹 LoadTester
- Envía peticiones aleatorias a `/predict` cada segundo

### 🔹 Prometheus
- Scrapea métricas expuestas por la API

### 🔹 Grafana
- Visualiza métricas desde Prometheus

### 🔹 GitHub Actions
- Entrena modelo
- Construye y sube imágenes Docker
- Automatiza el pipeline CI/CD

### 🔹 Argo CD
- GitOps: sincroniza manifiestos directamente desde el repositorio

---

## 🚀 Despliegue Local (Opcional)

```bash
kubectl apply -k Niveles/4/manifests/
kubectl apply -f Niveles/4/argo-cd/app.yaml
```

### 🔎 Acceder a los servicios

```bash
kubectl port-forward svc/api 8000:80
kubectl port-forward svc/grafana 3000:3000
kubectl port-forward svc/prometheus 9090:9090
```

- FastAPI: [http://localhost:8000/docs](http://localhost:8000/docs)
- Prometheus: [http://localhost:9090](http://localhost:9090)
- Grafana: [http://localhost:3000](http://localhost:3000)

---

## ✅ Requisitos

- Docker
- Kubernetes o Minikube
- GitHub Actions activado
- Argo CD desplegado en el clúster
- Acceso a DockerHub y GitHub

![image](https://github.com/user-attachments/assets/4eea16bc-1f6d-466a-9643-d7ced6d3a619)

![image](https://github.com/user-attachments/assets/33635476-8fe8-41ea-bdc8-d2aef5b59124)

