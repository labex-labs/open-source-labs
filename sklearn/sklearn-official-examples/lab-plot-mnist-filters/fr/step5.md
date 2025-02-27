# Entraîner le MLPClassifier

Nous allons créer un MLPClassifier avec une seule couche cachée contenant 40 neurones. Nous allons entraîner le MLP pour seulement 8 itérations en raison de contraintes de ressources. Nous capturerons également l'`Avertissement de convergence` qui sera levé car le modèle ne convergera pas dans le nombre limité d'itérations.

```python
mlp = MLPClassifier(
    hidden_layer_sizes=(40,),
    max_iter=8,
    alpha=1e-4,
    solver="sgd",
    verbose=10,
    random_state=1,
    learning_rate_init=0.2,
)

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=ConvergenceWarning, module="sklearn")
    mlp.fit(X_train, y_train)
```
