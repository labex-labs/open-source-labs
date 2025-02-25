# Obtener y Establecer Opciones

Podemos obtener o establecer el valor de una sola opción utilizando `pd.get_option` o `pd.set_option` respectivamente. Aquí, estamos estableciendo el número máximo de filas de visualización en 999.

```python
# Obtener la configuración actual para el número máximo de filas de visualización
print(pd.options.display.max_rows)

# Establecer el número máximo de filas de visualización en 999
pd.options.display.max_rows = 999

# Verificar la nueva configuración
print(pd.options.display.max_rows)
```
