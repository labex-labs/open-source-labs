# 이론적 한계 (계속)

두 번째 플롯은 허용 가능한 왜곡 `eps`가 증가함에 따라 주어진 샘플 수 `n_samples`에 대해 최소 차원 `n_components`를 줄일 수 있음을 보여줍니다.

```python
# 허용 가능한 왜곡의 범위
eps_range = np.linspace(0.01, 0.99, 100)

# 임베딩할 샘플 수 (관측치) 의 범위
n_samples_range = np.logspace(2, 6, 5)
colors = plt.cm.Blues(np.linspace(0.3, 1.0, len(n_samples_range)))

plt.figure()
for n_samples, color in zip(n_samples_range, colors):
    min_n_components = johnson_lindenstrauss_min_dim(n_samples, eps=eps_range)
    plt.semilogy(eps_range, min_n_components, color=color)

plt.legend([f"n_samples = {n}" for n in n_samples_range], loc="upper right")
plt.xlabel("왜곡 eps")
plt.ylabel("최소 차원 수")
plt.title("존슨 - 린덴슈트라우스 한계:\nn_components 대 eps")
plt.show()
```
