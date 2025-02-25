# Posicionar las anotaciones

Podemos posicionar las anotaciones utilizando diferentes sistemas de coordenadas. El siguiente código posicionará la anotación de texto utilizando coordenadas de datos y la anotación de flecha utilizando coordenadas de fracción de figura.

```python
ax.annotate("Punto de datos 1", xy=(1, 3), xytext=(1.5, 3.5),
            arrowprops=dict(facecolor="black", shrink=0.05),
            xycoords="data", textcoords="data")
ax.annotate("", xy=(1, 3), xytext=(0.5, 0.5),
            arrowprops=dict(facecolor="black", shrink=0.05),
            xycoords="data", textcoords="figure fraction")
```
