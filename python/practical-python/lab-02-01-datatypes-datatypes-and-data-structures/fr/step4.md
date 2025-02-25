# Tuples

Un tuple est une collection de valeurs regroupées ensemble.

Exemple :

```python
s = ('GOOG', 100, 490.1)
```

Parfois, les `()` sont omis dans la syntaxe.

```python
s = 'GOOG', 100, 490.1
```

Cas spéciaux (0-tuple, 1-tuple).

```python
t = ()            # Un tuple vide
w = ('GOOG', )    # Un tuple à un élément
```

Les tuples sont souvent utilisés pour représenter des enregistrements ou des structures _simples_. En général, c'est un seul _objet_ composé de plusieurs parties. Une bonne analogie : _Un tuple est comme une seule ligne dans un tableau de base de données._

Le contenu d'un tuple est ordonné (comme un tableau).

```python
s = ('GOOG', 100, 490.1)
name = s[0]                 # 'GOOG'
shares = s[1]               # 100
price = s[2]                # 490.1
```

Cependant, le contenu ne peut pas être modifié.

```python
>>> s[1] = 75
TypeError: object does not support item assignment
```

Cependant, vous pouvez créer un nouveau tuple à partir d'un tuple existant.

```python
s = (s[0], 75, s[2])
```
