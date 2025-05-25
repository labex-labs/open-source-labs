# Personalizando o Gráfico

Agora que criamos um gráfico básico, vamos personalizá-lo para torná-lo mais visualmente atraente. Podemos adicionar um título, rótulos de eixo e alterar a cor e o estilo da linha.

```python
# Add title and axis labels
plt.title('Sin Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Change color and style of line
plt.plot(x, y, color='red', linestyle='dashed')
plt.show()
```
