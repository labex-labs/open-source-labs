# Modelo com Remoção de Metadados

Agora, usaremos a opção `remove` do carregador de dados 20 newsgroups no scikit-learn para treinar um classificador de texto que não dependa demasiado dos metadados para tomar suas decisões. Também analisaremos os erros de classificação em um conjunto de teste usando uma matriz de confusão e inspecionaremos os coeficientes que definem a função de classificação dos modelos treinados.

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
    f"Matriz de Confusão para {clf.__class__.__name__}\nos documentos filtrados"
)

_ = plot_feature_effects().set_title("Efeitos médios das características nos documentos filtrados")
```
