# Espaces de noms

Un module est une collection de valeurs nommées et est parfois appelé un _espace de noms_. Les noms sont toutes les variables globales et les fonctions définies dans le fichier source. Après l'importation, le nom du module est utilisé comme préfixe. D'où l'_espace de noms_.

```python
import foo

a = foo.grok(2)
b = foo.spam('Hello')
...
```

Le nom du module est directement lié au nom de fichier (foo -> foo.py).
