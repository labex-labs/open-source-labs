# Enregistrez le graphique

Vous pouvez enregistrer le graphique sous forme de fichier image à l'aide de la méthode `savefig`. Le code suivant enregistre le graphique sous forme d'image PNG :

```python
plt.plot([1, 2, 3, 4], 'o-r')
plt.title('Simple Plot')
plt.xlabel('Index')
plt.ylabel('Numbers')
plt.savefig('simple_plot.png')
```
