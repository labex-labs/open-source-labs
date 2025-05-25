# Criando Múltiplos Gráficos

Também podemos criar múltiplos gráficos na mesma figura.

```python
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title('Plot 1')

plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title('Plot 2')

plt.show()
```

Aqui, estamos usando a função `subplot` para criar dois gráficos lado a lado na mesma figura. Passamos três argumentos para `subplot`: o número de linhas, o número de colunas e o número do gráfico. Em seguida, criamos um gráfico em cada subplot.
