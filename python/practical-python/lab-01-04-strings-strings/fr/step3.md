# Représentation de chaînes de caractères

Chaque caractère dans une chaîne est stocké en interne sous la forme d'un soi-disant "point de code" Unicode, qui est un entier. Vous pouvez spécifier une valeur exacte de point de code à l'aide des séquences d'échappement suivantes :

```python
a = '\xf1'          # a = 'ñ'
b = '\u2200'        # b = '∀'
c = '\U0001D122'    # c = '𝄢'
d = '\N{FOR ALL}'   # d = '∀'
```

La [Unicode Character Database](https://unicode.org/charts) est une référence pour tous les codes de caractères disponibles.
