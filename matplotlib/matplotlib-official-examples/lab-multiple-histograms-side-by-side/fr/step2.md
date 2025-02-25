# Créez des ensembles de données d'exemple

Ensuite, nous allons créer des ensembles de données d'exemple pour les utiliser dans nos histogrammes. Nous allons créer trois ensembles de données avec 387 points de données chacun :

```python
np.random.seed(19680801)
number_of_data_points = 387
labels = ["A", "B", "C"]
data_sets = [np.random.normal(0, 1, number_of_data_points),
             np.random.normal(6, 1, number_of_data_points),
             np.random.normal(-3, 1, number_of_data_points)]
```
