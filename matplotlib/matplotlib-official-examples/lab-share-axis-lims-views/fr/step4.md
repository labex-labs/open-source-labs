# Créez la deuxième figure

Ensuite, nous allons créer la deuxième figure. Nous utiliserons `subplot` à nouveau, mais cette fois-ci, nous définirons l'attribut `sharex` sur la première figure (`ax1`). Cela garantit que la deuxième figure partagera le même axe x que la première figure.

```python
ax2 = plt.subplot(212, sharex=ax1)
ax2.plot(t, np.sin(4*np.pi*t))
```
