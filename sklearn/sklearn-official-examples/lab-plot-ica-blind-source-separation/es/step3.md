# Graficar los resultados

Graficaremos la señal mixta original, las fuentes independientes originales, las fuentes estimadas por ICA y las fuentes estimadas por PCA.

```python
import matplotlib.pyplot as plt

plt.figure()

models = [X, S, S_, H]
names = [
    "Observaciones (señal mixta)",
    "Fuentes reales",
    "Señales recuperadas por ICA",
    "Señales recuperadas por PCA",
]
colors = ["rojo", "azul acero", "naranja"]

for ii, (model, name) in enumerate(zip(models, names), 1):
    plt.subplot(4, 1, ii)
    plt.title(name)
    for sig, color in zip(model.T, colors):
        plt.plot(sig, color=color)

plt.tight_layout()
plt.show()
```
