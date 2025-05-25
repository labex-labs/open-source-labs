# Personalizar o Gráfico

Podemos personalizar o gráfico para torná-lo mais visualmente atraente. Neste exemplo, adicionaremos um título, rótulos de eixo e mudaremos a cor do gráfico.

```python
# Customize the plot
ax.set_title('Wireframe Plot')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5, color='green')
```
