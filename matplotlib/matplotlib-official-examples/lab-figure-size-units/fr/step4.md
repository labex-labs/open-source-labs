# Taille de la figure en pixels

Nous pouvons également spécifier la taille de la figure en pixels. Pour ce faire, nous devons convertir la valeur en pixels en pouces. Nous pouvons obtenir le facteur de conversion de pixels en pouces en divisant 1 par la valeur de dpi (points par pouce). Nous pouvons ensuite utiliser cette valeur comme paramètre figsize dans la fonction subplots. Le code ci-dessous montre comment créer une figure d'une taille de 600 pixels x 200 pixels.

```python
px = 1/plt.rcParams['figure.dpi']  # pixel en pouces
plt.subplots(figsize=(600*px, 200*px))
plt.show()
```
