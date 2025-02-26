# Retourner des valeurs optionnelles

Parfois, une fonction peut retourner une valeur optionnelle - éventuellement comme un mécanisme pour indiquer le succès ou l'échec. La convention la plus courante est d'utiliser `None` pour représenter une valeur manquante. Modifiez la fonction `parse_line()` ci-dessus de sorte qu'elle retourne soit un tuple en cas de succès, soit `None` en cas de données invalides. Par exemple :

```python
>>> parse_line('email=guido@python.org')
('email', 'guido@python.org')
>>> parse_line('spam')       # Retourne None
>>>
```

Discussion sur la conception : Est-il meilleur que la fonction `parse_line()` lève une exception en cas de données malformées?
