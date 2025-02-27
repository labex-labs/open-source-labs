# Daten laden und vorbereiten

Als nächstes laden und bereiten wir die Daten vor. Wir laden den Iris-Datensatz mit scikit-learn und wählen nur zwei Merkmale aus. Anschließend teilen wir die Daten in einen Trainingssatz und einen Testsatz auf.

```python
n_neighbors = 1

dataset = datasets.load_iris()
X, y = dataset.data, dataset.target

# we only take two features. We could avoid this ugly
# slicing by using a two-dim dataset
X = X[:, [0, 2]]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.7, random_state=42
)
```
