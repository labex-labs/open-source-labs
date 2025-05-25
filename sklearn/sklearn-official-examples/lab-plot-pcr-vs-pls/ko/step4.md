# 회귀자 비교

PCR 및 PLS 회귀자 모두에 대해 첫 번째 구성 요소에 투영된 데이터를 대상과 함께 플롯합니다. 두 경우 모두 투영된 데이터가 회귀자가 학습 데이터로 사용할 데이터입니다.

```python
fig, axes = plt.subplots(1, 2, figsize=(10, 3))
axes[0].scatter(pca.transform(X_test), y_test, alpha=0.3, label="ground truth")
axes[0].scatter(
    pca.transform(X_test), pcr.predict(X_test), alpha=0.3, label="predictions"
)
axes[0].set(
    xlabel="첫 번째 주성분으로 투영된 데이터", ylabel="y", title="PCR / PCA"
)
axes[0].legend()
axes[1].scatter(pls.transform(X_test), y_test, alpha=0.3, label="ground truth")
axes[1].scatter(
    pls.transform(X_test), pls.predict(X_test), alpha=0.3, label="predictions"
)
axes[1].set(xlabel="첫 번째 PLS 구성요소로 투영된 데이터", ylabel="y", title="PLS")
axes[1].legend()
plt.tight_layout()
plt.show()
```

두 추정기의 R-제곱 점수를 출력합니다. 이는 이 경우 PLS 가 PCR 보다 더 나은 대안임을 추가로 확인합니다.

```python
print(f"PCR r-squared {pcr.score(X_test, y_test):.3f}")
print(f"PLS r-squared {pls.score(X_test, y_test):.3f}")
```
