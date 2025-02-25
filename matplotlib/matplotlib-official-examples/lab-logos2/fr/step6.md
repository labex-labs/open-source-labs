# Affichage des logos

Dans cette étape, nous allons afficher les logos de Matplotlib de différentes tailles.

```python
# Un grand logo :
make_logo(height_px=110, lw_bars=0.7, lw_grid=0.5, lw_border=1,
          rgrid=[1, 3, 5, 7])

# Un petit logo de 32px :
make_logo(height_px=32, lw_bars=0.3, lw_grid=0.3, lw_border=0.3, rgrid=[5])

# Un grand logo incluant le texte, tel que utilisé sur le site web de Matplotlib.
make_logo(height_px=110, lw_bars=0.7, lw_grid=0.5, lw_border=1,
          rgrid=[1, 3, 5, 7], with_text=True)
plt.show()
```
