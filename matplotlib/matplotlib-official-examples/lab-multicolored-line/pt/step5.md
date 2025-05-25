# Criar uma Barra de Cores

Criaremos uma barra de cores para mostrar o mapeamento entre as cores e os valores de `dydx`. Usaremos a função `colorbar` de `matplotlib.pyplot` para criar uma barra de cores.

```python
line = plt.gca().add_collection(lc)
plt.colorbar(line)
```
