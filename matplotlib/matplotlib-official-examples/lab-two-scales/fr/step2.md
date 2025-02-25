# Créez des données fictives

Ensuite, nous allons créer des données fictives pour nos graphiques. Nous utiliserons `numpy.arange` pour créer un tableau de valeurs allant de 0,01 à 10,0 avec un pas de 0,01. Nous utiliserons ensuite `numpy.exp` et `numpy.sin` pour créer deux ensembles de données.

```python
# Create some mock data
t = np.arange(0.01, 10.0, 0.01)
data1 = np.exp(t)
data2 = np.sin(2 * np.pi * t)
```
