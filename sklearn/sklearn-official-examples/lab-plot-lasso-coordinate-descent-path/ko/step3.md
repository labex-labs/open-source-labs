# 양수 Lasso 를 이용한 정규화 경로 계산

이 단계에서는 양수 Lasso 기법을 사용하여 정규화 경로를 계산하고 matplotlib 를 사용하여 결과를 표시합니다.

```python
# 양수 Lasso 를 이용하여 정규화 경로 계산
alphas_positive_lasso, coefs_positive_lasso, _ = lasso_path(X, y, eps=eps, positive=True)

# matplotlib 를 사용하여 결과 표시
plt.figure(2)
neg_log_alphas_positive_lasso = -np.log10(alphas_positive_lasso)
for coef_l, coef_pl, c in zip(coefs_lasso, coefs_positive_lasso, colors):
    l1 = plt.plot(neg_log_alphas_lasso, coef_l, c=c)
    l2 = plt.plot(neg_log_alphas_positive_lasso, coef_pl, linestyle="--", c=c)

plt.xlabel("-Log(alpha)")
plt.ylabel("계수")
plt.title("Lasso 및 양수 Lasso")
plt.legend((l1[-1], l2[-1]), ("Lasso", "양수 Lasso"), loc="lower left")
plt.axis("tight")
plt.show()
```
