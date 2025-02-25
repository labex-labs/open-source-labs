# Declaración continue

Para omitir un elemento y pasar al siguiente, utiliza la declaración `continue`.

```python
for line in lines:
    if line == '\n':    # Omite líneas en blanco
        continue
    # Más declaraciones
 ...
```

Esto es útil cuando el elemento actual no es de interés o debe ser ignorado en el procesamiento.
