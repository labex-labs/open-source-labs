# Plotar Pontuação Univariada das Características

Podemos plotar as pontuações univariadas para cada característica para ver quais características são significativas.

```python
import matplotlib.pyplot as plt

X_indices = np.arange(X.shape[-1])
plt.figure(1)
plt.clf()
plt.bar(X_indices - 0.05, scores, width=0.2)
plt.title("Pontuação univariada das características")
plt.xlabel("Número da característica")
plt.ylabel(r"Pontuação univariada ($-Log(p_{value})$)")
plt.show()
```
