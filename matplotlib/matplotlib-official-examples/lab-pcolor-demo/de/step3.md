# Pcolor mit logarithmischer Skala

Der dritte Schritt besteht darin, einen Pcolor-Plot mit logarithmischer Skala zu erstellen. Dies ist nützlich, wenn Sie Daten mit einem großen Wertebereich haben.

```python
N = 100
X, Y = np.meshgrid(np.linspace(-3, 3, N), np.linspace(-2, 2, N))

# Ein niedriger Buckel mit einem Ausläufer.
# Braucht eine logarithmische Skala auf der z/Farbachse, damit wir sowohl den Buckel als auch den Ausläufer sehen.
# Eine lineare Skala zeigt nur den Ausläufer.
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X * 10)**2 - (Y * 10)**2)
Z = Z1 + 50 * Z2

fig, (ax0, ax1) = plt.subplots(2, 1)

c = ax0.pcolor(X, Y, Z, shading='auto',
               norm=LogNorm(vmin=Z.min(), vmax=Z.max()), cmap='PuBu_r')
fig.colorbar(c, ax=ax0)

c = ax1.pcolor(X, Y, Z, cmap='PuBu_r', shading='auto')
fig.colorbar(c, ax=ax1)

plt.show()
```
