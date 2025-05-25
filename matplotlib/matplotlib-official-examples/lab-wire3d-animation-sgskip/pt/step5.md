# Animar o Gráfico

O quinto passo é animar o gráfico. Usaremos um loop `for` para iterar através de uma faixa de valores para phi. Em cada iteração, removeremos a coleção de linhas anterior, geraremos novos dados, plotaremos o novo wireframe e faremos uma pausa brevemente antes de continuar.

```python
wframe = None
tstart = time.time()
for phi in np.linspace(0, 180. / np.pi, 100):
    if wframe:
        wframe.remove()
    Z = np.cos(2 * np.pi * X + phi) * (1 - np.hypot(X, Y))
    wframe = ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2)
    plt.pause(.001)
```
