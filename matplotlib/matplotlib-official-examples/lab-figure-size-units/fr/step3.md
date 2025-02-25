# Taille de la figure en centimètres

Nous pouvons également spécifier la taille de la figure en centimètres. Pour ce faire, nous devons convertir les nombres basés sur les centimètres en pouces. Nous pouvons le faire en multipliant la valeur en centimètres par le facteur de conversion de cm en pouces, qui est 1/2,54. Nous pouvons ensuite utiliser cette valeur comme paramètre figsize dans la fonction subplots. Le code ci-dessous montre comment créer une figure d'une taille de 15 cm x 5 cm.

```python
cm = 1/2.54  # centimètres en pouces
plt.subplots(figsize=(15*cm, 5*cm))
plt.show()
```
