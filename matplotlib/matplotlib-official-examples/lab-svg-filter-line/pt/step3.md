# Desenhar Linhas

Desenhamos duas linhas usando `ax.plot()`. Também personalizamos as linhas com diferentes cores, marcadores e rótulos.

```python
l1, = ax.plot([0.1, 0.5, 0.9], [0.1, 0.9, 0.5], "bo-", mec="b", lw=5, ms=10, label="Line 1")
l2, = ax.plot([0.1, 0.5, 0.9], [0.5, 0.2, 0.7], "rs-", mec="r", lw=5, ms=10, label="Line 2")
```
