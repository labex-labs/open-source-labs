# Chargez ou générez de petits ensembles de données

Maintenant, nous devons charger ou générer les petits ensembles de données que nous utiliserons pour cet exemple. Nous utiliserons l'ensemble de données iris, l'ensemble de données digits et deux ensembles de données générés à l'aide des fonctions make_circles et make_moons.

```python
iris = datasets.load_iris()
X_digits, y_digits = datasets.load_digits(return_X_y=True)
data_sets = [
    (iris.data, iris.target),
    (X_digits, y_digits),
    datasets.make_circles(noise=0.2, factor=0.5, random_state=1),
    datasets.make_moons(noise=0.3, random_state=0),
]
```
