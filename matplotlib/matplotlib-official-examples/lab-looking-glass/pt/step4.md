# Plotando os Dados

Plotaremos os dados aleatórios gerados no Passo 2 usando a função `plot()` duas vezes. O primeiro gráfico terá um valor alpha de 0.2 e o segundo gráfico terá um valor alpha de 1.0 e um caminho de recorte (clip path) definido para o patch de círculo amarelo.

```python
ax.plot(x, y, alpha=0.2)
line, = ax.plot(x, y, alpha=1.0, clip_path=circ)
ax.set_title("Left click and drag to move looking glass")
```
