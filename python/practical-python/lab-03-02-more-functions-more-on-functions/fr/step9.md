# Variables globales

Les fonctions peuvent librement accéder aux valeurs des variables globales définies dans le même fichier.

```python
name = 'Dave'

def greeting():
    print('Hello', name)  # Utilisation de la variable globale `name`
```

Cependant, les fonctions ne peuvent pas modifier les variables globales :

```python
name = 'Dave'

def spam():
  name = 'Guido'

spam()
print(name) # Affiche 'Dave'
```

**Rappel : Toutes les affectations dans les fonctions sont locales.**
