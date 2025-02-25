# Crear la figura y los subgráficos

Necesitamos crear una figura y subgráficos para mostrar los datos. En este laboratorio, crearemos dos subgráficos, uno al lado del otro.

```python
# Figure width is doubled (2*6.4) to display nicely 2 subplots side by side.
fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(7, 9.6))
for ax in (ax0, ax1):
    ax.set_xscale('log')
```
