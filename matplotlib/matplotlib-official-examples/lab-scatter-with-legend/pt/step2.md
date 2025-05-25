# Criando um Gráfico de Dispersão com Múltiplos Grupos

Podemos criar um gráfico de dispersão com múltiplos grupos iterando sobre cada grupo e criando um gráfico de dispersão para aquele grupo. Especificamos a cor, o tamanho e a transparência dos marcadores para cada grupo usando os parâmetros `c`, `s` e `alpha`, respectivamente. Também definimos o parâmetro `label` para o nome do grupo, que será usado na legenda.

```python
fig, ax = plt.subplots()
for color in ['tab:blue', 'tab:orange', 'tab:green']:
    n = 750
    x, y = np.random.rand(2, n)
    scale = 200.0 * np.random.rand(n)
    ax.scatter(x, y, c=color, s=scale, label=color,
               alpha=0.3, edgecolors='none')

ax.legend()
ax.grid(True)

plt.show()
```
