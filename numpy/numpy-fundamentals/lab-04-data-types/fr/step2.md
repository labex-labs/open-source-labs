# Travailler avec les types de données

Les types de données de NumPy sont représentés sous forme d'objets `dtype` (type de données). Une fois que vous avez importé NumPy en utilisant `import numpy as np`, vous pouvez accéder aux types de données en utilisant `np.bool_`, `np.float32`, etc.

Vous pouvez utiliser les types de données comme des fonctions pour convertir des nombres Python en scalaires de tableau, des séquences Python de nombres en tableaux de ce type, ou comme arguments pour le mot clé dtype dans de nombreuses fonctions ou méthodes de NumPy. Voici quelques exemples :

```python
x = np.float32(1.0)
# x est maintenant un scalaire de tableau float32 avec la valeur 1.0

y = np.int_([1,2,4])
# y est maintenant un tableau d'entiers avec les valeurs [1, 2, 4]

z = np.arange(3, dtype=np.uint8)
# z est maintenant un tableau uint8 avec les valeurs [0, 1, 2]
```

Vous pouvez également vous référer aux types de tableau à l'aide de codes caractères, bien que l'utilisation d'objets dtype soit recommandée. Par exemple :

```python
np.array([1, 2, 3], dtype='f')
# renvoie un tableau avec les valeurs [1., 2., 3.] et le dtype float32
```

Pour convertir le type d'un tableau, vous pouvez utiliser la méthode `.astype()` ou le type lui-même comme fonction. Par exemple :

```python
z.astype(float)
# renvoie le tableau z avec le dtype float64

np.int8(z)
# renvoie le tableau z avec le dtype int8
```
