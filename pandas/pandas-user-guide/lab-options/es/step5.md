# Usando option_context

La función `option_context` nos permite ejecutar un bloque de código con un conjunto de opciones que se restauran a las configuraciones anteriores después de la ejecución.

```python
# Ejecutar un bloque de código con un conjunto de opciones
with pd.option_context("display.max_rows", 10):
    # Esto imprimirá 10 a pesar de que la configuración global sea diferente
    print(pd.get_option("display.max_rows"))

# Esto imprimirá la configuración global ya que el bloque de contexto ha terminado
print(pd.get_option("display.max_rows"))
```
