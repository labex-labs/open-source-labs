# Plotar um Histograma 2D

Para plotar um histograma 2D, basta ter dois vetores do mesmo comprimento, correspondentes a cada eixo do histograma.

```python
fig, ax = plt.subplots(tight_layout=True)
hist = ax.hist2d(dist1, dist2)

plt.show()
```
