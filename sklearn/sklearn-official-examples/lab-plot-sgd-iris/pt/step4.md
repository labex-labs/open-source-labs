# Plotar Pontos de Treinamento

Agora, plotaremos os pontos de treinamento na superfície de decisão. Usaremos o método `scatter()` para plotar os pontos de treinamento com cores diferentes para valores-alvo diferentes.

```python
for i, color in zip(clf.classes_, colors):
    idx = np.where(y == i)
    plt.scatter(
        X[idx, 0],
        X[idx, 1],
        c=color,
        label=iris.target_names[i],
        cmap=plt.cm.Paired,
        edgecolor="black",
        s=20,
    )
plt.title("Superfície de decisão de SGD multi-classe")
plt.axis("tight")
```
