# Salvando o Gráfico

Depois de criarmos um gráfico, podemos salvá-lo em um arquivo.

```python
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.title('My Plot')
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.savefig('my_plot.png')
```

Aqui, estamos usando a função `savefig` para salvar nosso gráfico em um arquivo chamado `my_plot.png`.
