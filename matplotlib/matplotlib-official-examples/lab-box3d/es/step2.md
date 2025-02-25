# Crea datos falsos

Crea datos falsos para graficar utilizando una fórmula para calcular los datos basados en los valores de X, Y y Z. Le agregaremos uno al resultado para asegurar que el valor mínimo sea mayor que cero.

```python
# Crea datos falsos
data = (((X+100)**2 + (Y-20)**2 + 2*Z)/1000+1)
```
