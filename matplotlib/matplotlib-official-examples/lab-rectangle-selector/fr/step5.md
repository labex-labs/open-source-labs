# Tracez quelque chose sur les sous-graphiques

Nous allons tracer quelque chose sur les sous-graphiques afin que l'utilisateur puisse voir l'effet du RectangleSelector et de l'EllipseSelector.

```python
N = 100000  # If N is large one can see improvement by using blitting.
x = np.linspace(0, 10, N)

for ax in axs:
    ax.plot(x, np.sin(2*np.pi*x))  # plot something
```
