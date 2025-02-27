# Diskretisierung des Eingangsmerkmals

In diesem Schritt verwenden wir die Klasse KBinsDiscretizer, um das Eingangsmerkmal zu diskretisieren. Wir werden 10 Bins erstellen und die One-Hot-Codierung verwenden, um die Daten zu transformieren.

```python
enc = KBinsDiscretizer(n_bins=10, encode="onehot")
X_binned = enc.fit_transform(X)
```
