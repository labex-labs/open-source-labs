# Criar o gráfico

Crie um objeto de figura e eixo usando `subplots`. Plote os valores de x e y usando `plot`. Defina os limites do eixo y para começar em 0 usando `set_ylim`.

```python
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ax.set_ylim(bottom=0)
```
