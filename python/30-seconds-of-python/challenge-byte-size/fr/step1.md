# Taille en octets d'une chaîne de caractères

## Problème

Écrivez une fonction `byte_size(s)` qui prend une chaîne de caractères `s` en entrée et renvoie sa taille en octets. La taille en octets d'une chaîne est le nombre d'octets nécessaires pour stocker la chaîne en mémoire. Pour calculer la taille en octets d'une chaîne, vous devez encoder la chaîne en utilisant un schéma d'encodage spécifique. Dans ce défi, vous utiliserez le schéma d'encodage UTF-8.

Pour calculer la taille en octets d'une chaîne, vous pouvez suivre ces étapes :

1. Encodez la chaîne en utilisant le schéma d'encodage UTF-8.
2. Obtenez la longueur de la chaîne encodée.

Votre fonction devrait renvoyer la longueur de la chaîne encodée.

## Exemple

```python
byte_size('😀') # 4
byte_size('Hello World') # 11
```

Dans l'exemple ci-dessus, la taille en octets de la chaîne `'😀'` est 4 car il faut 4 octets pour stocker la version encodée en UTF-8 de la chaîne en mémoire. La taille en octets de la chaîne `'Hello World'` est 11 car il faut 11 octets pour stocker la version encodée en UTF-8 de la chaîne en mémoire.
