# Fizz Buzz

## Problem

Implementiere Fizz Buzz mit Python. Ihre Funktion sollte eine ganze Zahl n als Eingabe entgegennehmen und eine Liste von Strings zurückgeben, die die Zahlen von 1 bis n darstellen, mit folgenden Modifikationen:

- Vielfache von 3 sollten durch den String "Fizz" ersetzt werden
- Vielfache von 5 sollten durch den String "Buzz" ersetzt werden
- Vielfache von sowohl 3 als auch 5 sollten durch den String "FizzBuzz" ersetzt werden

Ihre Funktion sollte auch die folgenden Fälle behandeln:

- Wenn die Eingabe kleiner als 1 ist, werfe eine Ausnahme
- Wenn die Eingabe keine gültige ganze Zahl ist, werfe eine Ausnahme

## Anforderungen

Um Fizz Buzz in Python zu implementieren, müssen wir die folgenden Anforderungen beachten:

- Definiere eine Funktion, die eine ganze Zahl n als Eingabe entgegennimmt
- Überprüfe, ob die Eingabe eine gültige ganze Zahl ist und werfe eine Ausnahme, wenn nicht
- Überprüfe, ob die Eingabe kleiner als 1 ist und werfe eine Ausnahme, wenn ja
- Erstelle eine Liste von Strings, die die Zahlen von 1 bis n darstellen, mit den oben beschriebenen Modifikationen
- Gebe die Liste zurück

## Beispielverwendung

```python
assert fizz_buzz(15) == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
```

```python
try:
    fizz_buzz(0)
except ValueError:
    print("Ungültige Eingabe")
```

```python
try:
    fizz_buzz("hello")
except ValueError:
    print("Ungültige Eingabe")
```

```python
try:
    fizz_buzz(-5)
except ValueError:
    print("Ungültige Eingabe")
```
