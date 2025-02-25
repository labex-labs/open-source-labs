# Vergleich von Pcolor mit ähnlichen Funktionen

Der zweite Schritt besteht darin, Pcolor mit ähnlichen Funktionen wie Pcolormesh, Imshow und Pcolorfast zu vergleichen. Dies wird Ihnen helfen, die Unterschiede zwischen diesen Funktionen zu verstehen und wann Sie jede von ihnen verwenden sollten.

```python
# Verkleinern Sie diese Werte, um die Auflösung zu erhöhen
dx, dy = 0.15, 0.05

# Generieren Sie 2 2D-Gitter für die x- und y-Begrenzungen
y, x = np.mgrid[-3:3+dy:dy, -3:3+dx:dx]
z = (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)
# x und y sind die Begrenzungen, daher sollte z der Wert *innerhalb* dieser Begrenzungen sein.
# Entfernen Sie daher den letzten Wert aus dem z-Array.
z = z[:-1, :-1]
z_min, z_max = -abs(z).max(), abs(z).max()

fig, axs = plt.subplots(2, 2)

ax = axs[0, 0]
c = ax.pcolor(x, y, z, cmap='RdBu', vmin=z_min, vmax=z_max)
ax.set_title('pcolor')
fig.colorbar(c, ax=ax)

ax = axs[0, 1]
c = ax.pcolormesh(x, y, z, cmap='RdBu', vmin=z_min, vmax=z_max)
ax.set_title('pcolormesh')
fig.colorbar(c, ax=ax)

ax = axs[1, 0]
c = ax.imshow(z, cmap='RdBu', vmin=z_min, vmax=z_max,
              extent=[x.min(), x.max(), y.min(), y.max()],
              interpolation='nearest', origin='lower', aspect='auto')
ax.set_title('Bild (nächstes, aspect="auto")')
fig.colorbar(c, ax=ax)

ax = axs[1, 1]
c = ax.pcolorfast(x, y, z, cmap='RdBu', vmin=z_min, vmax=z_max)
ax.set_title('pcolorfast')
fig.colorbar(c, ax=ax)

fig.tight_layout()
plt.show()
```
