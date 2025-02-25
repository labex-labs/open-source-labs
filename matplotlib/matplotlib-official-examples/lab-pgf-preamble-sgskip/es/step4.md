# Personalizar el gráfico

Puedes personalizar el gráfico cambiando los colores, los estilos de línea y los marcadores. Aquí hay un ejemplo:

```python
plt.plot(x, y1, 'r--', label='sin')
plt.plot(x, y2, 'g:', label='cos')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine and Cosine Functions')
plt.legend()
plt.show()
```
