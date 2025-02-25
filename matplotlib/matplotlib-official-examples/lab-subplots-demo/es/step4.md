# Compartir ejes

Por defecto, cada `Axes` se escala individualmente. Para alinear el eje horizontal o vertical de los subgráficos, podemos utilizar los parámetros `sharex` o `sharey`.

```python
fig, (ax1, ax2) = plt.subplots(2, sharex=True)
ax1.plot(x, y)
ax2.plot(x + 1, -y)
```
