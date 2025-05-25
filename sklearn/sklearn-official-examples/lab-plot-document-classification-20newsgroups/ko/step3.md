# 메타데이터 제거 모델

이제 scikit-learn 의 20 뉴스그룹 데이터셋 로더의 `remove` 옵션을 사용하여 메타데이터에 지나치게 의존하지 않는 텍스트 분류기를 학습시킵니다. 또한 혼동 행렬을 사용하여 테스트 세트의 분류 오류를 분석하고, 학습된 모델의 분류 함수를 정의하는 계수를 검사합니다.

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

_ = plot_feature_effects().set_title("Filtered documents 의 평균 특징 효과")
```
