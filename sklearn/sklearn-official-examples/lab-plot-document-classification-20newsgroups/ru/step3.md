# Модель с удалением метаданных

Теперь мы будем использовать параметр `remove` загрузчика датасета 20 newsgroups в scikit-learn для обучения текстового классификатора, который не слишком сильно зависит от метаданных при принятии решений. Также мы будем анализировать ошибки классификации на тестовом наборе с использованием матрицы неточностей и изучать коэффициенты, которые определяют функцию классификации обученных моделей.

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
    f"Confusion Matrix for {clf.__class__.__name__}\non filtered documents"
)

_ = plot_feature_effects().set_title("Average feature effects on filtered documents")
```
