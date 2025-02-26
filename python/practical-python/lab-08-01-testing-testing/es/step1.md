# Aserciones

La declaración `assert` es una comprobación interna para el programa. Si una expresión no es verdadera, lanza una excepción `AssertionError`.

Sintaxis de la declaración `assert`.

```python
assert <expresión> [, 'Mensaje de diagnóstico']
```

Por ejemplo.

```python
assert isinstance(10, int), 'Se esperaba un int'
```

No debe usarse para comprobar la entrada del usuario (es decir, los datos ingresados en un formulario web o algo por el estilo). Su propósito es más para comprobaciones internas e invariantes (condiciones que siempre deben ser verdaderas).
