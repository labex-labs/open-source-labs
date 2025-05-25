# Personalizando as marcas e rótulos

Personalizaremos as marcas (ticks) e os rótulos dos eixos usando o método `ax1.tick_params()`. Definiremos a cor, a rotação e o tamanho do rótulo do eixo x, e a cor, o tamanho e a largura das marcas do eixo y.

```python
ax1.tick_params(axis='x', labelcolor='tab:red', labelrotation=45, labelsize=16)
ax1.tick_params(axis='y', color='tab:green', size=25, width=3)
```
