# Zufällige Daten generieren

Wir werden zwei Sets von zufälligen Daten mit der `random.normal`-Funktion von NumPy generieren. Diese Sets werden verwendet, um Histogramme mit unterschiedlichen Stilen zu erstellen.

```python
np.random.seed(19680801)

mu_x = 200
sigma_x = 25
x = np.random.normal(mu_x, sigma_x, size=100)

mu_w = 200
sigma_w = 10
w = np.random.normal(mu_w, sigma_w, size=100)
```
