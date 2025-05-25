# Plotar o Conjunto de Dados Ponderado

Plotamos o conjunto de dados ponderado utilizando a biblioteca matplotlib. O tamanho dos pontos é proporcional ao seu peso.

```python
xx, yy = np.meshgrid(np.linspace(-4, 5, 500), np.linspace(-4, 5, 500))
fig, ax = plt.subplots()
ax.scatter(
    X[:, 0],
    X[:, 1],
    c=y,
    s=sample_weight,
    alpha=0.9,
    cmap=plt.cm.bone,
    edgecolor="black",
)
```
