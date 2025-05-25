# Formatando o Estilo do Gráfico

Em seguida, vamos personalizar o estilo do nosso gráfico. Podemos usar o terceiro argumento opcional da função `plot` para especificar a string de formato, que indica a cor e o tipo de linha do gráfico. Por exemplo, vamos plotar o mesmo gráfico de linha com círculos vermelhos:

```python
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()
```

Explicação:

- Usamos a string de formato `'ro'` para indicar círculos vermelhos para o gráfico.
- A função `axis` é usada para definir a janela de visualização dos eixos, especificando a faixa de valores para os eixos x e y.
