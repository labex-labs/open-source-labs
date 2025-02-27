# Préparer les données pour l'apprentissage semi-supervisé

Nous sélectionnons 340 échantillons et seulement 40 de ces échantillons sont associés à une étiquette connue. Nous stockons les indices des 300 autres échantillons pour lesquels nous ne sommes pas supposés connaître leurs étiquettes. Nous mélangeons ensuite les étiquettes de sorte que les échantillons non étiquetés soient marqués avec -1.

```python
X = digits.data[indices[:340]]
y = digits.target[indices[:340]]

n_total_samples = len(y)
n_labeled_points = 40

indices = np.arange(n_total_samples)

unlabeled_set = indices[n_labeled_points:]

y_train = np.copy(y)
y_train[unlabeled_set] = -1
```
