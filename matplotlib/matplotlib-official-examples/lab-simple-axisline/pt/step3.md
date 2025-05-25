# Ocultar Eixos Superior e Direito

Agora, ocultaremos os eixos superior e direito, pois só precisamos dos eixos esquerdo e inferior.

```python
ax.axis["right"].set_visible(False)
ax.axis["top"].set_visible(False)
```
