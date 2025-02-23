#Comparer le comportement de "symlog" et "asinh" sur un graphique d'échantillonnage y=x

Nous allons comparer le comportement de "symlog" et "asinh" sur un graphique d'échantillonnage y=x. Nous allons tracer le même graphique deux fois, une fois avec "symlog" et une fois avec "asinh".

```python
fig1 = plt.figure()
ax0, ax1 = fig1.subplots(1, 2, sharex=True)

ax0.plot(x, x)
ax0.set_yscale('symlog')
ax0.grid()
ax0.set_title('symlog')

ax1.plot(x, x)
ax1.set_yscale('asinh')
ax1.grid()
ax1.set_title('asinh')
```
