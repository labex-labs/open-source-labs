# Modèle avec élimination des métadonnées

Nous allons maintenant utiliser l'option `remove` du chargeur d'ensemble de données 20 newsgroups dans scikit-learn pour entraîner un classifieur de texte qui ne dépend pas trop des métadonnées pour prendre ses décisions. Nous allons également analyser les erreurs de classification sur un ensemble de test en utilisant une matrice de confusion et examiner les coefficients qui définissent la fonction de classification des modèles entraînés.

```python
(
    X_train,
    X_test,
    y_train,
    y_test,
    feature_names,
    target_names,
) = load_dataset(remove=("headers", "footers", "quotes"))

clf = RidgeClassifier(tol=1e-2, solver="sparse_cg")
clf.fit(X_train, y_train)
pred = clf.predict(X_test)

fig, ax = plt.subplots(figsize=(10, 5))
ConfusionMatrixDisplay.from_predictions(y_test, pred, ax=ax)
ax.xaxis.set_ticklabels(target_names)
ax.yaxis.set_ticklabels(target_names)
_ = ax.set_title(
    f"Matrice de confusion pour {clf.__class__.__name__}\n sur les documents filtrés"
)

_ = plot_feature_effects().set_title("Effets moyens des caractéristiques sur les documents filtrés")
```
