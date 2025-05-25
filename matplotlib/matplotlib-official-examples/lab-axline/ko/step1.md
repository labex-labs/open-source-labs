# 수직 및 수평선 그리기

`axvline`과 `axhline`을 사용하여 각각 수직선과 수평선을 그릴 수 있습니다. `y=0`, `y=0.5`, 그리고 `y=1.0`에서 세 개의 수평선을 그려보겠습니다.

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
