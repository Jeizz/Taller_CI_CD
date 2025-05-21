from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
import pickle
import os

X, y = make_regression(n_samples=100, n_features=1, noise=0.1)
model = LinearRegression().fit(X, y)

os.makedirs("app", exist_ok=True)
with open("app/model.pkl", "wb") as f:
    pickle.dump(model, f)
print("Modelo entrenado y guardado en 'app/model.pkl'")
