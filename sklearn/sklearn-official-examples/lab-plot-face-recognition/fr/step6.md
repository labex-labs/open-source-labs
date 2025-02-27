# Évaluer les performances du modèle

```python
y_pred = clf.predict(X_test_pca)
print(classification_report(y_test, y_pred, target_names=target_names))
ConfusionMatrixDisplay.from_estimator(
    clf, X_test_pca, y_test, display_labels=target_names, xticks_rotation="vertical"
)
```

Nous prédisons les valeurs cibles en utilisant les données de test et évaluons les performances du modèle à l'aide de la fonction `classification_report()`. Nous traçons également la matrice de confusion à l'aide de la fonction `ConfusionMatrixDisplay()`.
