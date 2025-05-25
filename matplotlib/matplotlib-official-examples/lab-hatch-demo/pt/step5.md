# Criar um Gráfico com Patches Hachurados

Você também pode usar hachuras com patches em seu gráfico. Neste caso, usaremos a função `fill_between` para criar um patch hachurado.

```python
x = np.arange(0, 40, 0.2)
plt.fill_between(x, np.sin(x) * 4 + 30, y2=0, hatch='///', zorder=2, fc='c')
```
