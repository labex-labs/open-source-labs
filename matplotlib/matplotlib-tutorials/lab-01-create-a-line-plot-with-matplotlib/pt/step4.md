# Personalizar o gráfico

Podemos personalizar o gráfico adicionando rótulos aos eixos x e y, um título ao gráfico e uma legenda. Também podemos alterar o estilo e a cor da linha.

```python
plt.plot(x, y, linestyle='--', color='red', label='sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Line Plot')
plt.legend()
```
