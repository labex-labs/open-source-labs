# 서브플롯 플롯

이 단계에서는 `plot_subfigure` 함수를 사용하여 서브플롯을 그립니다.

```python
plt.figure(figsize=(8, 6))

plot_subfigure(X, Y, 1, "레이블 없는 샘플 포함 + CCA", "cca")
plot_subfigure(X, Y, 2, "레이블 없는 샘플 포함 + PCA", "pca")

X, Y = make_multilabel_classification(
    n_classes=2, n_labels=1, allow_unlabeled=False, random_state=1
)

plot_subfigure(X, Y, 3, "레이블 없는 샘플 제외 + CCA", "cca")
plot_subfigure(X, Y, 4, "레이블 없는 샘플 제외 + PCA", "pca")

plt.subplots_adjust(0.04, 0.02, 0.97, 0.94, 0.09, 0.2)
plt.show()
```
