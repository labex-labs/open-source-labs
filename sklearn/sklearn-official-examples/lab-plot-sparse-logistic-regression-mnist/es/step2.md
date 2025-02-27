# Cargar el conjunto de datos MNIST

Cargaremos el conjunto de datos MNIST usando la función `fetch_openml` de scikit-learn. También seleccionaremos un subconjunto de los datos fijando el número de `train_samples` en 5000.

```python
# Turn down for faster convergence
t0 = time.time()
train_samples = 5000

# Load data from https://www.openml.org/d/554
X, y = fetch_openml(
    "mnist_784", version=1, return_X_y=True, as_frame=False, parser="pandas"
)
```
