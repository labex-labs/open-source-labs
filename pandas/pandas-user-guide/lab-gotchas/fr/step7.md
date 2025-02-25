# Gérer les problèmes d'ordre d'octets

Vous pouvez rencontrer des problèmes d'ordre d'octets lorsqu'il s'agit de traiter des données créées sur une machine ayant un ordre d'octets différent. Convertissez les données en ordre d'octets natif du système avant de les passer à Pandas.

```python
x = np.array(list(range(10)), ">i4")  # big endian
newx = x.byteswap().newbyteorder()  # force native byteorder
s = pd.Series(newx)
```
