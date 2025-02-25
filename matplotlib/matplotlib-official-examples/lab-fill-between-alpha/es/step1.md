# Mejora de un gráfico de líneas con `fill_between`

El primer ejemplo demuestra cómo mejorar un gráfico de líneas con `fill_between`. Utilizaremos datos financieros de Google para crear dos subgráficos, uno con un gráfico de líneas simple y el otro con un gráfico de líneas relleno.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook

# carga algunos datos financieros de muestra
r = cbook.get_sample_data('goog.npz')['price_data'].view(np.recarray)

# crea dos subgráficos con los ejes x e y compartidos
fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True)

pricemin = r.close.min()

ax1.plot(r.date, r.close, lw=2)
ax2.fill_between(r.date, pricemin, r.close, alpha=0.7)

for ax in ax1, ax2:
    ax.grid(True)
    ax.label_outer()

ax1.set_ylabel('precio')
fig.suptitle('Precio de cierre diario de Google (GOOG)')
fig.autofmt_xdate()
```
