# Compartilhando Eixos

Por padrão, cada `Axes` é escalado individualmente. Para alinhar o eixo horizontal ou vertical de subplots, podemos usar os parâmetros `sharex` ou `sharey`.

```python
fig, (ax1, ax2) = plt.subplots(2, sharex=True)
ax1.plot(x, y)
ax2.plot(x + 1, -y)
```
