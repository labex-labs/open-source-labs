# Daten generieren

Wir werden einen künstlichen Datensatz generieren, bei dem der Zielwert positiv mit der ersten Eigenschaft und negativ mit der zweiten Eigenschaft korreliert ist. Wir werden auch etwas zufälliges Rauschen hinzufügen, um die Daten realistischer zu machen.

```python
rng = np.random.RandomState(0)

n_samples = 1000
f_0 = rng.rand(n_samples)
f_1 = rng.rand(n_samples)
X = np.c_[f_0, f_1]
noise = rng.normal(loc=0.0, scale=0.01, size=n_samples)

y = 5 * f_0 + np.sin(10 * np.pi * f_0) - 5 * f_1 - np.cos(10 * np.pi * f_1) + noise
```
