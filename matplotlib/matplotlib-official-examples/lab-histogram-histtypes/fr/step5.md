# Modifiez le style de l'histogramme

Nous pouvons modifier le style de l'histogramme en spécifiant le paramètre `histtype` dans la fonction `hist`. Dans cet exemple, nous allons créer un histogramme avec une courbe en escalier qui a une couleur de remplissage.

```python
plt.hist(x, bins=20, density=True, histtype='stepfilled', facecolor='g', alpha=0.75)
plt.show()
```
