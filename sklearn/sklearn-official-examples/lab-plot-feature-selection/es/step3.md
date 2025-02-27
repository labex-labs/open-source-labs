# Graficar la puntuación univariada de las características

Podemos graficar las puntuaciones univariadas de cada característica para ver cuáles son las características significativas.

```python
import matplotlib.pyplot as plt

X_indices = np.arange(X.shape[-1])
plt.figure(1)
plt.clf()
plt.bar(X_indices - 0.05, scores, width=0.2)
plt.title("Puntuación univariada de la característica")
plt.xlabel("Número de característica")
plt.ylabel(r"Puntuación univariada ($-Log(p_{valor})$)")
plt.show()
```
