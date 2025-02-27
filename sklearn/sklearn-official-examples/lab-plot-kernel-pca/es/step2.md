# Visualizar el conjunto de datos

Graficaremos el conjunto de datos generado utilizando matplotlib para visualizar el conjunto de datos.

```python
import matplotlib.pyplot as plt

_, (train_ax, test_ax) = plt.subplots(ncols=2, sharex=True, sharey=True, figsize=(8, 4))

train_ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train)
train_ax.set_ylabel("Característica #1")
train_ax.set_xlabel("Característica #0")
train_ax.set_title("Datos de entrenamiento")

test_ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
test_ax.set_xlabel("Característica #0")
_ = test_ax.set_title("Datos de prueba")
```
