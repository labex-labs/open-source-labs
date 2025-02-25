# Fixez la graine aléatoire et générez des données

Nous utiliserons numpy pour générer des données aléatoires. Pour que nos résultats soient reproductibles, nous allons fixer une graine aléatoire. Ajoutez le code suivant à votre fichier :

```python
np.random.seed(19680801)
data = np.random.randn(1000)
```
