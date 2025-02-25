# Taille en octets d'une chaîne de caractères

Écrivez une fonction `byte_size(s)` qui prend une chaîne de caractères `s` en entrée et renvoie sa taille en octets. La taille en octets d'une chaîne est le nombre d'octets nécessaires pour stocker la chaîne en mémoire. Pour calculer la taille en octets d'une chaîne, vous devez encoder la chaîne en utilisant un schéma d'encodage spécifique. Dans ce laboratoire, vous utiliserez le schéma d'encodage UTF-8.

Pour calculer la taille en octets d'une chaîne, vous pouvez suivre ces étapes :

1. Encoder la chaîne en utilisant le schéma d'encodage UTF-8.
2. Obtenir la longueur de la chaîne encodée.

Votre fonction devrait renvoyer la longueur de la chaîne encodée.

```python
def byte_size(s):
  return len(s.encode('utf-8'))
```

```python
byte_size('😀') # 4
byte_size('Hello World') # 11
```
