# Plotar os Dados

Nesta etapa, plotaremos os dados de exemplo que geramos na etapa anterior. Usaremos um loop `for` para plotar múltiplas ondas senoidais com diferentes fases.

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
