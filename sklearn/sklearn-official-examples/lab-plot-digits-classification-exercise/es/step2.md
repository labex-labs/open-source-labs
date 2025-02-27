# Preprocesar los datos

Luego preprocesaremos los datos escalando las características a un rango de [0, 1] utilizando el valor máximo de los datos. Esto se puede hacer dividiendo los datos de entrada por el valor máximo de los datos de entrada.

```python
X_digits = X_digits / X_digits.max()
```
