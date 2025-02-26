# Manejo de Excepciones

Las excepciones se propagan hasta el primer `except` que coincide.

```python
def grok():
  ...
    raise RuntimeError('Whoa!')   # Se lanza la excepción aquí

def spam():
    grok()                        # Llamada que causará la excepción

def bar():
    try:
       spam()
    except RuntimeError as e:     # Se captura la excepción aquí
      ...

def foo():
    try:
         bar()
    except RuntimeError as e:     # La excepción no llega aquí
      ...

foo()
```

Para manejar la excepción, coloca las instrucciones en el bloque `except`. Puedes agregar cualquier instrucción que desees para manejar el error.

```python
def grok():...
    raise RuntimeError('Whoa!')

def bar():
    try:
      grok()
    except RuntimeError as e:   # Se captura la excepción aquí
        instrucciones           # Utiliza estas instrucciones
        instrucciones
      ...

bar()
```

Después de manejar la excepción, la ejecución continúa con la primera instrucción después del `try-except`.

```python
def grok():...
    raise RuntimeError('Whoa!')

def bar():
    try:
      grok()
    except RuntimeError as e:   # Se captura la excepción aquí
        instrucciones
        instrucciones
      ...
    instrucciones                  # Continúa la ejecución aquí
    instrucciones                  # Y sigue aquí
  ...

bar()
```
