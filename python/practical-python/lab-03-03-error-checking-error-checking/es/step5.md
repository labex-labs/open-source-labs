# Valores de Excepción

Las excepciones tienen un valor asociado. Contiene información más específica sobre lo que está mal.

```python
raise RuntimeError('Invalid user name')
```

Este valor es parte de la instancia de excepción que se coloca en la variable suministrada a `except`.

```python
try:
 ...
except RuntimeError as e:   # `e` contiene la excepción generada
 ...
```

`e` es una instancia del tipo de excepción. Sin embargo, a menudo parece una cadena cuando se imprime.

```python
except RuntimeError as e:
    print('Failed : Reason', e)
```
