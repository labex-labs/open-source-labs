# Affichage

La fonction `print` produit une seule ligne de texte avec les valeurs passées.

```python
print('Hello world!') # Affiche le texte 'Hello world!'
```

Vous pouvez utiliser des variables. Le texte affiché sera la valeur de la variable, pas le nom.

```python
x = 100
print(x) # Affiche le texte '100'
```

Si vous passez plus d'une valeur à `print`, elles sont séparées par des espaces.

```python
name = 'Jake'
print('My name is', name) # Affiche le texte 'My name is Jake'
```

`print()` met toujours un retour à la ligne à la fin.

```python
print('Hello')
print('My name is', 'Jake')
```

Cela affiche :

```code
Hello
My name is Jake
```

Le retour à la ligne supplémentaire peut être supprimé :

```python
print('Hello', end=' ')
print('My name is', 'Jake')
```

Ce code affichera maintenant :

```code
Hello My name is Jake
```
