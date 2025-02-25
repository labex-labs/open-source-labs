# Utilisation des feuilles de style

Une autre manière de modifier l'apparence visuelle des graphiques est de définir les paramètres rc dans une feuille de style et d'importer cette feuille de style avec `matplotlib.style.use`. Une feuille de style est un fichier qui contient un ensemble de paramètres rc liés au style d'un graphique. Matplotlib propose un certain nombre de styles prédéfinis que vous pouvez utiliser. Par exemple, le style "ggplot" imite l'esthétique de la bibliothèque ggplot en R. Vous pouvez appliquer une feuille de style comme ceci :

```python
import matplotlib.pyplot as plt

print(plt.style.available)
plt.style.use('Solarize_Light2')
```

Vous pouvez également définir vos propres styles personnalisés et les utiliser en appelant `.style.use` avec le chemin ou l'URL de la feuille de style.
