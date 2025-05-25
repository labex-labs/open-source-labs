# Adicionar o rótulo da integral

Adicione o rótulo da integral ao gráfico usando `text`. O rótulo deve ser centralizado no ponto médio entre a e b e deve ser formatado usando mathtext.

```python
ax.text(0.5 * (a + b), 30, r"$\int_a^b f(x)\mathrm{d}x$",
        horizontalalignment='center', fontsize=20)
```
