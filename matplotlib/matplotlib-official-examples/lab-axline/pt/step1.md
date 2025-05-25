# Desenhar linhas verticais e horizontais

Podemos usar `axvline` e `axhline` para desenhar linhas verticais e horizontais, respectivamente. Vamos desenhar três linhas horizontais em `y=0`, `y=0.5` e `y=1.0`.

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

# Plot sigmoid function
plt.plot(t, sig, linewidth=2, label=r"$\sigma(t) = \frac{1}{1 + e^{-t}}$")
plt.xlim(-10, 10)
plt.xlabel("t")
plt.legend(fontsize=14)
plt.show()
```
