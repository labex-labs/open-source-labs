# Récupérer le type de données d'un tableau

Pour déterminer le type de données d'un tableau, vous pouvez accéder à l'attribut `dtype`. Par exemple :

```python
z.dtype
# renvoie le dtype du tableau z, qui est uint8
```

L'objet `dtype` contient également des informations sur le type, telles que sa largeur en bits et son ordre d'octets. Vous pouvez utiliser l'objet `dtype` pour interroger les propriétés du type, par exemple pour savoir s'il s'agit d'un entier. Par exemple :

```python
d = np.dtype(int)
# crée un objet dtype pour int

np.issubdtype(d, np.integer)
# renvoie True, indiquant que d est un sous-type de np.integer

np.issubdtype(d, np.floating)
# renvoie False, indiquant que d n'est pas un sous-type de np.floating
```
