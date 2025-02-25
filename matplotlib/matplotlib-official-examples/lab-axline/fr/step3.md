# Tracer une ligne arbitraire

Nous pouvons utiliser `axline` pour tracer une ligne dans n'importe quelle direction. Traçons une ligne avec une pente de `0,25` passant par le point `(0, 0,5)`.

```python
import matplotlib.pyplot as plt
import numpy as np

# Générer des données
t = np.linspace(-10, 10, 100)
sig = 1 / (1 + np.exp(-t))

# Tracer des lignes horizontales
plt.axhline(y=0, color="black", linestyle="--")
plt.axhline(y=0.5, color="black", linestyle=":")
plt.axhline(y=1.0, color="black", linestyle="--")

# Tracer la ligne verticale
plt.axvline(color="grey")

# Tracer la ligne arbitraire
plt.axline((0, 0.5), slope=0.25, color="black", linestyle=(0, (5, 5)))

# Tracer la fonction sigmoïde
plt.plot(t, sig, linewidth=2, label=r"$\sigma(t) = \frac{1}{1 + e^{-t}}$")
plt.xlim(-10, 10)
plt.xlabel("t")
plt.legend(fontsize=14)
plt.show()
```
