# Ensemble de données

Nous utiliserons l'ensemble de données 20 newsgroups, qui est composé de messages de groupes de discussion sur 20 sujets. L'ensemble de données est divisé en sous-ensembles d'entraînement et de test en fonction des messages postés avant et après une date spécifique. Nous n'utiliserons que les messages de 2 catégories pour accélérer le temps d'exécution.

```python
categories = ["sci.med", "sci.space"]
X_train, y_train = fetch_20newsgroups(
    random_state=1,
    subset="train",
    categories=categories,
    remove=("footers", "quotes"),
    return_X_y=True,
)
X_test, y_test = fetch_20newsgroups(
    random_state=1,
    subset="test",
    categories=categories,
    remove=("footers", "quotes"),
    return_X_y=True,
)
```
