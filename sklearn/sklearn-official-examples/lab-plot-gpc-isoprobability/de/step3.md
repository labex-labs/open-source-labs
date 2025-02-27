# Modell trainieren

Wir werden ein GPC-Modell verwenden, um die Daten zu klassifizieren. Zunächst müssen wir die Kernfunktion angeben.

```python
kernel = C(0.1, (1e-5, np.inf)) * DotProduct(sigma_0=0.1) ** 2
```

Anschließend können wir ein GPC-Modell erstellen und es mit den Daten trainieren.

```python
gp = GaussianProcessClassifier(kernel=kernel)
gp.fit(X, y)
```
