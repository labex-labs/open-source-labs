# Plotten der Daten

In diesem Schritt werden wir die Beispiel-Daten plotten, die wir im vorherigen Schritt generiert haben. Wir werden eine `for`-Schleife verwenden, um mehrere Sinuswellen mit unterschiedlichen Phasen zu plotten.

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
