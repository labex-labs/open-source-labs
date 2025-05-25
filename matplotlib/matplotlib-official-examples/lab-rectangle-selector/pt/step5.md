# Plotar algo nos subplots

Plotaremos algo nos subplots, para que o usuário possa ver o efeito do `RectangleSelector` e do `EllipseSelector`.

```python
N = 100000  # If N is large one can see improvement by using blitting.
x = np.linspace(0, 10, N)

for ax in axs:
    ax.plot(x, np.sin(2*np.pi*x))  # plot something
```
