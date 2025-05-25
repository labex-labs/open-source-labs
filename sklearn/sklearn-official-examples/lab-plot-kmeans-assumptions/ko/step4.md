# 가능한 해결책

K-평균 군집화의 한계를 극복하기 위한 몇 가지 해결책을 논의할 것입니다. 다음 코드 블록에서는 첫 번째 데이터셋에 대한 올바른 클러스터 수를 찾는 방법과 불균일한 크기의 볼록을 처리하기 위해 여러 번의 랜덤 초기화를 수행하는 방법을 보여줍니다.

```python
y_pred = KMeans(n_clusters=3, **common_params).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.title("최적의 클러스터 수")
plt.show()

y_pred = KMeans(n_clusters=3, n_init=10, random_state=random_state).fit_predict(
    X_filtered
)
plt.scatter(X_filtered[:, 0], X_filtered[:, 1], c=y_pred)
plt.title("불균일 크기 볼록 \n여러 초기화")
plt.show()
```
