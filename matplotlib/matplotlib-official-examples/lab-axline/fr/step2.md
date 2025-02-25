# Tracer une ligne verticale

Nous pouvons utiliser `axvline` pour tracer une ligne verticale à une position `x` donnée. Dessinons une ligne verticale à `x = 0`.

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

# Tracer la fonction sigmoïde
plt.plot(t, sig, linewidth=2, label=r"$\sigma(t) = \frac{1}{1 + e^{-t}}$")
plt.xlim(-10, 10)
plt.xlabel("t")
plt.legend(fontsize=14)
plt.show()
```
