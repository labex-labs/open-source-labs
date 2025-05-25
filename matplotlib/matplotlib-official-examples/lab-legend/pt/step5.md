# Estilizando a Legenda

Finalmente, podemos estilizar a legenda para torná-la mais visualmente atraente. Usamos a função `get_frame` para obter o frame da legenda e, em seguida, usamos a função `set_facecolor` para definir a cor de fundo do frame.

```python
# Put a nicer background color on the legend.
legend.get_frame().set_facecolor('C0')
```
