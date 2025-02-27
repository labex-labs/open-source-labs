# Visualización de datos

En este paso, visualizaremos los datos generados.

```python
import matplotlib.pyplot as plt

plt.plot(X, y, label="Señal esperada")
plt.legend()
plt.xlabel("X")
_ = plt.ylabel("y")
```
