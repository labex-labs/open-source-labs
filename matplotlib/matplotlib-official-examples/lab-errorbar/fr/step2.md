# Créez des données d'exemple

Ensuite, nous allons créer des données d'exemple pour les utiliser dans le graphique. Dans cet exemple, nous utiliserons la fonction `numpy.arange()` pour créer un tableau de valeurs compris entre 0,1 et 4 avec un pas de 0,5. Nous utiliserons ensuite la fonction `numpy.exp()` pour calculer l'exponentielle de chaque valeur dans le tableau.

```python
# example data
x = np.arange(0.1, 4, 0.5)
y = np.exp(-x)
```
