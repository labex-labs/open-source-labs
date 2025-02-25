# Definir valores de error

Ahora definiremos nuestros valores de error. En este ejemplo, usaremos la variable `error` para representar el error simétrico y la variable `asymmetric_error` para representar el error asimétrico.

```python
# example error bar values that vary with x-position
error = 0.1 + 0.2 * x

# error bar values w/ different -/+ errors that
# also vary with the x-position
lower_error = 0.4 * error
upper_error = error
asymmetric_error = [lower_error, upper_error]
```
