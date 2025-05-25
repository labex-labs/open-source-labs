# Personalizar o Gráfico

Você pode personalizar o gráfico alterando as cores, estilos de linha e marcadores. Aqui está um exemplo:

```python
plt.plot(x, y1, 'r--', label='sin')
plt.plot(x, y2, 'g:', label='cos')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine and Cosine Functions')
plt.legend()
plt.show()
```
