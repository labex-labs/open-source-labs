# Utiliser LassoCV pour vérifier la sélection d'alpha

Enfin, nous utiliserons LassoCV pour voir jusqu'à quel point nous pouvons faire confiance à la sélection d'alpha. Nous utiliserons KFold avec 3 plis.

```python
from sklearn.linear_model import LassoCV
from sklearn.model_selection import KFold

lasso_cv = LassoCV(alphas=alphas, random_state=0, max_iter=10000)
k_fold = KFold(3)

print("Réponse à la question bonus :", "jusqu'à quel point pouvez-vous faire confiance à la sélection d'alpha?")
print()
print("Paramètres alpha maximisant le score de généralisation sur différents")
print("sous-ensembles des données :")
for k, (train, test) in enumerate(k_fold.split(X, y)):
    lasso_cv.fit(X[train], y[train])
    print(
        "[pli {0}] alpha: {1:.5f}, score: {2:.5f}".format(
            k, lasso_cv.alpha_, lasso_cv.score(X[test], y[test])
        )
    )

print()
print("Réponse : Pas beaucoup puisque nous avons obtenu différents alphas pour différents")
print("sous-ensembles des données et de plus, les scores pour ces alphas diffèrent")
print("assez sensiblement.")
```
