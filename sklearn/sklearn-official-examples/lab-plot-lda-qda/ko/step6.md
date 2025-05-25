# 결정 경계 시각화

1 단계에서 생성된 데이터셋을 사용하여 LDA 와 QDA 의 결정 경계를 시각화합니다.

```python
plt.figure(figsize=(10, 8), facecolor="white")
plt.suptitle("선형 판별 분석 (LDA) 대 사차 판별 분석 (QDA)", y=0.98, fontsize=15)

for i, (X, y) in enumerate([dataset_fixed_cov(), dataset_cov()]):
    # 선형 판별 분석
    lda = LinearDiscriminantAnalysis(solver="svd", store_covariance=True)
    y_pred = lda.fit(X, y).predict(X)
    splot = plot_data(lda, X, y, y_pred, fig_index=2 * i + 1)
    plot_lda_cov(lda, splot)
    plt.axis("tight")

    # 사차 판별 분석
    qda = QuadraticDiscriminantAnalysis(store_covariance=True)
    y_pred = qda.fit(X, y).predict(X)
    splot = plot_data(qda, X, y, y_pred, fig_index=2 * i + 2)
    plot_qda_cov(qda, splot)
    plt.axis("tight")

plt.tight_layout()
plt.subplots_adjust(top=0.92)
plt.show()
```
