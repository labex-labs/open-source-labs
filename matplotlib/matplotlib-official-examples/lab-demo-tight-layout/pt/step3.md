# Personalizando o Gráfico

Agora que temos um gráfico básico, vamos personalizá-lo.

```python
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, color='red', marker='o')
plt.title('My Plot')
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.show()
```

Aqui, adicionamos algumas personalizações ao nosso gráfico. Mudamos a cor da linha para vermelho e adicionamos marcadores circulares a cada ponto de dados. Também adicionamos um título e rótulos de eixo ao nosso gráfico.
