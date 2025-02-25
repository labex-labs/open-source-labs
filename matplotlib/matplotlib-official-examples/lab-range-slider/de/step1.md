# Ein falsches Bild generieren

Zunächst werden wir ein falsches Graustufenbild mit dem Zufallsmodul von NumPy generieren. Wir werden den Seed setzen, um sicherzustellen, dass die Ergebnisse reproduzierbar sind.

```python
np.random.seed(19680801)
N = 128
img = np.random.randn(N, N)
```
