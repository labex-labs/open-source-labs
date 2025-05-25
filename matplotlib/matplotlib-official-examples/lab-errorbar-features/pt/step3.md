# Definir Valores de Erro

Agora definiremos nossos valores de erro. Neste exemplo, usaremos a variável `error` para representar o erro simétrico e a variável `asymmetric_error` para representar o erro assimétrico.

```python
# example error bar values that vary with x-position
error = 0.1 + 0.2 * x

# error bar values w/ different -/+ errors that
# also vary with the x-position
lower_error = 0.4 * error
upper_error = error
asymmetric_error = [lower_error, upper_error]
```
