# Modell mit Entfernung der Metadaten

Wir werden nun die `remove`-Option des 20 Newsgroups-Datensatz-Ladeprozedurs in scikit-learn verwenden, um einen Textklassifizierer zu trainieren, der bei seinen Entscheidungen nicht zu stark auf Metadaten angewiesen ist. Wir werden auch die Klassifizierungsfehler auf einem Testset mithilfe einer Konfusionsmatrix analysieren und die Koeffizienten untersuchen, die die Klassifizierungsfunktion der trainierten Modelle definieren.

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
    f"Konfusionsmatrix für {clf.__class__.__name__}\nauf gefilterten Dokumenten"
)

_ = plot_feature_effects().set_title("Durchschnittliche Feature-Effekte auf gefilterte Dokumente")
```
