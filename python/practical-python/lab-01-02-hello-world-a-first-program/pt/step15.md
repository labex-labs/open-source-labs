# Imprimindo (Printing)

A função `print` produz uma única linha de texto com os valores passados.

```python
print('Hello world!') # Prints the text 'Hello world!'
```

Você pode usar variáveis. O texto impresso será o valor da variável, não o nome.

```python
x = 100
print(x) # Prints the text '100'
```

Se você passar mais de um valor para `print`, eles são separados por espaços.

```python
name = 'Jake'
print('My name is', name) # Print the text 'My name is Jake'
```

`print()` sempre coloca uma nova linha no final.

```python
print('Hello')
print('My name is', 'Jake')
```

Isso imprime:

```code
Hello
My name is Jake
```

A nova linha extra pode ser suprimida:

```python
print('Hello', end=' ')
print('My name is', 'Jake')
```

Este código agora imprimirá:

```code
Hello My name is Jake
```
