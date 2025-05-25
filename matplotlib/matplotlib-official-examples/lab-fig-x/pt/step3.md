# Adicionar linhas à Figure

Podemos adicionar linhas à figura usando o método `fig.add_artist()`. Criaremos duas linhas - uma de (0,0) a (1,1) e outra de (0,1) a (1,0).

```python
fig.add_artist(lines.Line2D([0, 1], [0, 1]))
fig.add_artist(lines.Line2D([0, 1], [1, 0]))
```
