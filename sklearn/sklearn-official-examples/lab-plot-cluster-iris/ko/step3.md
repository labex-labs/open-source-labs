# 데이터 시각화

K-Means 군집화 알고리즘을 적용하기 전에 데이터를 시각화하여 더 잘 이해하는 것이 좋습니다. 3 차원 산점도를 사용하여 데이터를 시각화할 것입니다.

```python
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(X[:, 0], X[:, 1], X[:, 2])
ax.set_xlabel("꽃받침 길이")
ax.set_ylabel("꽃받침 폭")
ax.set_zlabel("꽃잎 길이")
plt.show()
```
