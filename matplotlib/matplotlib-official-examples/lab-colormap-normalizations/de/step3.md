# SymLogNorm

Wir werden zwei Buckelungen erstellen, eine negative und eine positive, wobei die positive Buckelung fünfmal die Amplitude hat. Linear können wir keine Details in der negativen Buckelung erkennen. Wir werden die positiven und negativen Daten separat logarithmisch skalieren, indem wir eine `SymLogNorm` verwenden.

```python
X, Y = np.mgrid[-3:3:complex(0, N), -2:2:complex(0, N)]
Z = 5 * np.exp(-X**2 - Y**2)

fig, ax = plt.subplots(2, 1)

pcm = ax[0].pcolormesh(X, Y, Z,
                       norm=colors.SymLogNorm(linthresh=0.03, linscale=0.03,
                                              vmin=-1.0, vmax=1.0, base=10),
                       cmap='RdBu_r', shading='nearest')
fig.colorbar(pcm, ax=ax[0], extend='both')

pcm = ax[1].pcolormesh(X, Y, Z, cmap='RdBu_r', vmin=-np.max(Z),
                       shading='nearest')
fig.colorbar(pcm, ax=ax[1], extend='both')
```
