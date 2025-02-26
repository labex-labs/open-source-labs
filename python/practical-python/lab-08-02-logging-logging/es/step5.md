# Configuración del registro

El comportamiento del registro se configura por separado.

```python
# main.py

...

if __name__ == '__main__':
    import logging
    logging.basicConfig(
        filename  = 'app.log',      # Archivo de salida del registro
        level     = logging.INFO,   # Nivel de salida
    )
```

Por lo general, esta es una configuración única al inicio del programa. La configuración es independiente del código que hace las llamadas de registro.
