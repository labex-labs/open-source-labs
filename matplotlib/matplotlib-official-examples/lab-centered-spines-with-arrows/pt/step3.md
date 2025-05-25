# Mover os spines

Por padrão, os _spines_ (bordas) são desenhados nas bordas do gráfico. Neste caso, você deseja mover os _spines_ esquerdo e inferior para o centro do gráfico.

```python
ax.spines[["left", "bottom"]].set_position(("data", 0))
```
