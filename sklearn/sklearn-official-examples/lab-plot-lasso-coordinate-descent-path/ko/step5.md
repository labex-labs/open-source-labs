# 양수 탄성 네트워크를 이용한 정규화 경로 계산

이 단계에서는 양수 탄성 네트워크 기법을 사용하여 정규화 경로를 계산하고 matplotlib 를 사용하여 결과를 표시합니다.

```python
# 양수 탄성 네트워크를 이용하여 정규화 경로 계산
alphas_positive_enet, coefs_positive_enet, _ = enet_path(X, y, eps=eps, l1_ratio=0.8, positive=True)

# matplotlib 를 사용하여 결과 표시
plt.figure(4)
neg_log_alphas_positive_enet = -np.log10(alphas_positive_enet)
for coef_e, coef_pe, c in zip(coefs_enet, coefs_positive_enet, colors):
    l1 = plt.plot(neg_log_alphas_enet, coef_e, c=c)
    l2 = plt.plot(neg_log_alphas_positive_enet, coef_pe, linestyle="--", c=c)

plt.xlabel("-Log(alpha)")
plt.ylabel("계수")
plt.title("탄성 네트워크 및 양수 탄성 네트워크")
plt.legend((l1[-1], l2[-1]), ("탄성 네트워크", "양수 탄성 네트워크"), loc="lower left")
plt.axis("tight")
plt.show()
```
