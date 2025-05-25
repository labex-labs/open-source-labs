# Plotar Resultados

Vamos plotar o sinal misto original, as fontes independentes originais, as fontes estimadas pelo ICA e as fontes estimadas pelo PCA.

```python
import matplotlib.pyplot as plt

plt.figure()

models = [X, S, S_, H]
names = [
    "Observações (sinal misto)",
    "Fontes verdadeiras",
    "Sinais recuperados pelo ICA",
    "Sinais recuperados pelo PCA",
]
colors = ["red", "steelblue", "orange"]

for ii, (model, name) in enumerate(zip(models, names), 1):
    plt.subplot(4, 1, ii)
    plt.title(name)
    for sig, color in zip(model.T, colors):
        plt.plot(sig, color=color)

plt.tight_layout()
plt.show()
```
