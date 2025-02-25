# Création du graphique en barres

Maintenant, nous sommes prêts à créer notre graphique en barres. Nous commencerons par définir quelques variables qui nous aideront à définir la largeur des barres et leur position sur l'axe x.

```python
dim = len(data[0])
w = 0.75
dimw = w / dim
```

Ensuite, nous créerons une figure et un objet d'axe à l'aide de la méthode `subplots()`. Ensuite, nous utiliserons une boucle `for` pour itérer sur chaque valeur de notre ensemble de données et créer une barre pour chacune d'entre elles.

```python
fig, ax = plt.subplots()
x = np.arange(len(data))
for i in range(len(data[0])):
    y = [d[i] for d in data]
    b = ax.bar(x + i * dimw, y, dimw, bottom=0.001)
```

Nous définissons le paramètre `bottom` sur `0.001` pour éviter d'avoir des barres de hauteur 0, ce qui n'est pas compatible avec une échelle logarithmique.
