# Dibujar una línea arbitraria

Podemos usar `axline` para dibujar una línea en cualquier dirección. Vamos a dibujar una línea con una pendiente de `0.25` que pasa por el punto `(0, 0.5)`.

```python
import matplotlib.pyplot as plt
import numpy as np

# Generate data
t = np.linspace(-10, 10, 100)
sig = 1 / (1 + np.exp(-t))

# Draw horizontal lines
plt.axhline(y=0, color="black", linestyle="--")
plt.axhline(y=0.5, color="black", linestyle=":")
plt.axhline(y=1.0, color="black", linestyle="--")

# Draw vertical line
plt.axvline(color="grey")

# Draw arbitrary line
plt.axline((0, 0.5), slope=0.25, color="black", linestyle=(0, (5, 5)))

# Plot sigmoid function
plt.plot(t, sig, linewidth=2, label=r"$\sigma(t) = \frac{1}{1 + e^{-t}}$")
plt.xlim(-10, 10)
plt.xlabel("t")
plt.legend(fontsize=14)
plt.show()
```
