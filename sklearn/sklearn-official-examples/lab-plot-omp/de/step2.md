# Die Daten generieren

```python
n_components, n_features = 512, 100
n_nonzero_coefs = 17

# die Daten generieren

# y = Xw
# |x|_0 = n_nonzero_coefs

y, X, w = make_sparse_coded_signal(
    n_samples=1,
    n_components=n_components,
    n_features=n_features,
    n_nonzero_coefs=n_nonzero_coefs,
    random_state=0,
)
X = X.T

(idx,) = w.nonzero()

# das saubere Signal verfälschen
y_noisy = y + 0.05 * np.random.randn(len(y))
```
