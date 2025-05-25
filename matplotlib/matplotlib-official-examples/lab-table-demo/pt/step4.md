# Criar Esquema de Cores

Criaremos um esquema de cores para a tabela usando a função `plt.cm.BuPu`. Usaremos tons pastéis de azul e roxo para as linhas.

```python
colors = plt.cm.BuPu(np.linspace(0, 0.5, len(rows)))
```
