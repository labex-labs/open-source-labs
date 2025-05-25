# 탄성 네트워크를 이용한 정규화 경로 계산

이 단계에서는 탄성 네트워크 (Elastic Net) 기법을 사용하여 정규화 경로를 계산하고 matplotlib 를 사용하여 결과를 표시합니다.

```python
from sklearn.linear_model import enet_path

# 탄성 네트워크를 이용하여 정규화 경로 계산
alphas_enet, coefs_enet, _ = enet_path(X, y, eps=eps, l1_ratio=0.8)

# matplotlib 를 사용하여 결과 표시
plt.figure(3)
neg_log_alphas_enet = -np.log10(alphas_enet)
for coef_e, c in zip(coefs_enet, colors):
    l1 = plt.plot(neg_log_alphas_enet, coef_e, c=c)

plt.xlabel("-Log(alpha)")
plt.ylabel("계수")
plt.title("탄성 네트워크 경로")
plt.axis("tight")
plt.show()
```
