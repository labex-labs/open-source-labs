# Créez et ajustez un arbre de décision AdaBoost

Dans cette étape, nous allons créer un arbre de décision AdaBoost à l'aide de la classe `AdaBoostClassifier` du module `sklearn.ensemble`. Nous utiliserons l'arbre de décision comme estimateur de base et définirons le paramètre `max_depth` sur 1. Nous définirons également le paramètre `algorithm` sur "SAMME" et le paramètre `n_estimators` sur 200. Enfin, nous ajusterons le classifieur à l'ensemble de données.

```python
bdt = AdaBoostClassifier(
    DecisionTreeClassifier(max_depth=1), algorithm="SAMME", n_estimators=200
)

bdt.fit(X, y)
```
