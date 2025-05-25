# Desenhar linhas diagonais

Podemos usar `axline` com o parâmetro `transform` para desenhar linhas diagonais com uma inclinação (slope) fixa. Vamos desenhar linhas de grade diagonais com uma inclinação fixa de `0.5`.

```python
import matplotlib.pyplot as plt
import numpy as np

# Draw diagonal lines
for pos in np.linspace(-2, 1, 10):
    plt.axline((pos, 0), slope=0.5, color='k', transform=plt.gca().transAxes)

plt.ylim([0, 1])
plt.xlim([0, 1])
plt.show()
```
