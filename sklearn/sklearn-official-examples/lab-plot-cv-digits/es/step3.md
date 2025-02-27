# Definir los valores de hiperparámetros para probar

Probaremos diferentes valores del parámetro de regularización C, que controla el equilibrio entre maximizar el margen y minimizar el error de clasificación. Probaremos 10 valores espaciados logarítmicamente entre 10^-10 y 1.

```python
C_s = np.logspace(-10, 0, 10)
```
