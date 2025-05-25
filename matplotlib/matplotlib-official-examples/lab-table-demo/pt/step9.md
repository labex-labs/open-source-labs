# Adicionar Rótulos de Eixo e Título

Adicionaremos rótulos de eixo e um título ao gráfico usando as funções `plt.ylabel`, `plt.yticks`, `plt.xticks` e `plt.title`.

```python
values = np.arange(0, 2500, 500)
value_increment = 1000

plt.ylabel(f"Loss in ${value_increment}'s")
plt.yticks(values * value_increment, ['%d' % val for val in values])
plt.xticks([])
plt.title('Loss by Disaster')
```
