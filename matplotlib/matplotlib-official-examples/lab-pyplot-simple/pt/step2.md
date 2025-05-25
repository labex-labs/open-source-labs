# Criar um Gráfico Simples

Para criar um gráfico simples em Matplotlib, você precisa fornecer uma lista de números que deseja plotar. Neste caso, plotaremos uma lista de números em relação ao seu índice, resultando em uma linha reta. Use uma string de formatação (aqui, 'o-r') para definir os marcadores (círculos), o estilo da linha (linha sólida) e a cor (vermelho).

```python
plt.plot([1, 2, 3, 4], 'o-r')
plt.ylabel('some numbers')
plt.show()
```
