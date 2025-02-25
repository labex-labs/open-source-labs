# Mostrando los logotipos

En este paso, mostraremos los logotipos de Matplotlib de diferentes tamaños.

```python
# Un logotipo grande:
make_logo(height_px=110, lw_bars=0.7, lw_grid=0.5, lw_border=1,
          rgrid=[1, 3, 5, 7])

# Un logotipo pequeño de 32px:
make_logo(height_px=32, lw_bars=0.3, lw_grid=0.3, lw_border=0.3, rgrid=[5])

# Un logotipo grande que incluye texto, como se utiliza en el sitio web de Matplotlib.
make_logo(height_px=110, lw_bars=0.7, lw_grid=0.5, lw_border=1,
          rgrid=[1, 3, 5, 7], with_text=True)
plt.show()
```
