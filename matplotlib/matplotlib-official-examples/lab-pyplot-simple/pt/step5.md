# Salvar o Gráfico

Você pode salvar o gráfico como um arquivo de imagem usando o método `savefig`. O código a seguir salva o gráfico como uma imagem PNG:

```python
plt.plot([1, 2, 3, 4], 'o-r')
plt.title('Simple Plot')
plt.xlabel('Index')
plt.ylabel('Numbers')
plt.savefig('simple_plot.png')
```
