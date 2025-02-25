# Imprimiendo

La función `print` produce una sola línea de texto con los valores pasados.

```python
print('Hello world!') # Imprime el texto 'Hello world!'
```

Puedes usar variables. El texto impreso será el valor de la variable, no el nombre.

```python
x = 100
print(x) # Imprime el texto '100'
```

Si pasas más de un valor a `print`, se separan por espacios.

```python
name = 'Jake'
print('My name is', name) # Imprime el texto 'My name is Jake'
```

`print()` siempre coloca un salto de línea al final.

```python
print('Hello')
print('My name is', 'Jake')
```

Esto imprime:

```code
Hello
My name is Jake
```

El salto de línea extra se puede suprimir:

```python
print('Hello', end=' ')
print('My name is', 'Jake')
```

Este código ahora imprimirá:

```code
Hello My name is Jake
```
