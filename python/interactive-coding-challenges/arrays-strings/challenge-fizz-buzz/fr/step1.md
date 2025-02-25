# Fizz Buzz

## Problème

Implémentez Fizz Buzz en utilisant Python. Votre fonction devrait prendre un entier `n` en entrée et renvoyer une liste de chaînes de caractères représentant les nombres de 1 à `n`, avec les modifications suivantes :

- Les multiples de 3 devraient être remplacés par la chaîne de caractères "Fizz"
- Les multiples de 5 devraient être remplacés par la chaîne de caractères "Buzz"
- Les multiples de 3 et 5 devraient être remplacés par la chaîne de caractères "FizzBuzz"

Votre fonction devrait également gérer les cas suivants :

- Si l'entrée est inférieure à 1, lever une exception
- Si l'entrée n'est pas un entier valide, lever une exception

## Exigences

Pour implémenter Fizz Buzz en Python, nous devons suivre ces exigences :

- Définir une fonction qui prend un entier `n` en entrée
- Vérifier si l'entrée est un entier valide et lever une exception si ce n'est pas le cas
- Vérifier si l'entrée est inférieure à 1 et lever une exception si c'est le cas
- Créer une liste de chaînes de caractères représentant les nombres de 1 à `n`, avec les modifications décrites ci-dessus
- Retourner la liste

## Utilisation de l'exemple

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
