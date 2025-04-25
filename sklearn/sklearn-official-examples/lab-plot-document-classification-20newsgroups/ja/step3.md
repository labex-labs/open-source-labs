# メタデータを削除したモデル

ここでは、scikit-learn の 20 ニュースグループデータセットローダーの`remove`オプションを使って、決定に際してメタデータに依存しないテキスト分類器を訓練します。また、混同行列を使ってテストセット上の分類エラーを分析し、訓練済みモデルの分類関数を定義する係数を調べます。

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
    f"混同行列 for {clf.__class__.__name__}\non filtered documents"
)

_ = plot_feature_effects().set_title("Average feature effects on filtered documents")
```
