# Fizz Buzz

## Problema

Implementa Fizz Buzz usando Python. Tu función debe tomar un entero `n` como entrada y devolver una lista de cadenas que representen los números del 1 al `n`, con las siguientes modificaciones:

- Los múltiplos de 3 deben ser reemplazados por la cadena "Fizz"
- Los múltiplos de 5 deben ser reemplazados por la cadena "Buzz"
- Los múltiplos de 3 y 5 deben ser reemplazados por la cadena "FizzBuzz"

Tu función también debe manejar los siguientes casos:

- Si la entrada es menor que 1, levanta una excepción
- Si la entrada no es un entero válido, levanta una excepción

## Requisitos

Para implementar Fizz Buzz en Python, debemos seguir estos requisitos:

- Definir una función que tome un entero `n` como entrada
- Verificar si la entrada es un entero válido y levantar una excepción si no lo es
- Verificar si la entrada es menor que 1 y levantar una excepción si lo es
- Crear una lista de cadenas que representen los números del 1 al `n`, con las modificaciones descritas anteriormente
- Devolver la lista

## Uso de ejemplo

```python
assert fizz_buzz(15) == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
```

```python
try:
    fizz_buzz(0)
except ValueError:
    print("Invalid input")
```

```python
try:
    fizz_buzz("hello")
except ValueError:
    print("Invalid input")
```

```python
try:
    fizz_buzz(-5)
except ValueError:
    print("Invalid input")
```
