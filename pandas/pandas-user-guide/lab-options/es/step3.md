# Restablecer Opciones

Si deseamos restablecer una o más opciones a su valor predeterminado, podemos utilizar `pd.reset_option`.

```python
# Restablecer el número máximo de filas de visualización al valor predeterminado
pd.reset_option("display.max_rows")

# Verificar el restablecimiento
print(pd.options.display.max_rows)
```
