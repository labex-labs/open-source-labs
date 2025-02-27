# Discretizar la característica de entrada

En este paso, utilizaremos la clase KBinsDiscretizer para discretizar la característica de entrada. Crearemos 10 intervalos (bins) y utilizaremos codificación one-hot para transformar los datos.

```python
enc = KBinsDiscretizer(n_bins=10, encode="onehot")
X_binned = enc.fit_transform(X)
```
