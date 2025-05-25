# Exibindo os Logotipos

Nesta etapa, exibiremos os logotipos do Matplotlib de diferentes tamanhos.

```python
# Um logotipo grande:
make_logo(height_px=110, lw_bars=0.7, lw_grid=0.5, lw_border=1,
          rgrid=[1, 3, 5, 7])

# Um logotipo pequeno de 32px:
make_logo(height_px=32, lw_bars=0.3, lw_grid=0.3, lw_border=0.3, rgrid=[5])

# Um logotipo grande incluindo texto, como usado no site do Matplotlib.
make_logo(height_px=110, lw_bars=0.7, lw_grid=0.5, lw_border=1,
          rgrid=[1, 3, 5, 7], with_text=True)
plt.show()
```
