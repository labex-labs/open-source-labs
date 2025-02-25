# Graficar los datos

En este paso, graficaremos los datos de muestra que generamos en el paso anterior. Usaremos un bucle `for` para graficar múltiples ondas sinusoidales con diferentes fases.

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
