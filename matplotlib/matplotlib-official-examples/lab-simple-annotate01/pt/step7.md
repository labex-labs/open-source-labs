# Posicionar Anotações

Podemos posicionar as anotações usando diferentes sistemas de coordenadas. O código a seguir posicionará a anotação de texto usando coordenadas de dados e a anotação de seta usando coordenadas da figura.

```python
ax.annotate("Data Point 1", xy=(1, 3), xytext=(1.5, 3.5),
            arrowprops=dict(facecolor="black", shrink=0.05),
            xycoords="data", textcoords="data")
ax.annotate("", xy=(1, 3), xytext=(0.5, 0.5),
            arrowprops=dict(facecolor="black", shrink=0.05),
            xycoords="data", textcoords="figure fraction")
```
