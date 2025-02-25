# Tracer les données

Dans cette étape, nous allons tracer les données d'échantillonnage que nous avons générées dans l'étape précédente. Nous utiliserons une boucle `for` pour tracer plusieurs ondes sinusoïdales avec des phases différentes.

```python
fig, ax = plt.subplots()

ncolors = len(plt.rcParams['axes.prop_cycle'])
shift = np.linspace(0, L, ncolors, endpoint=False)

for s in shift:
    # Plot the sine wave with a phase shift of s
    ax.plot(x, np.sin(x + s), 'o-')

ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_title("'dark_background' style sheet")

plt.show()
```
