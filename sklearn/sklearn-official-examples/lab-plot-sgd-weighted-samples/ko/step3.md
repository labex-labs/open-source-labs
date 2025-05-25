# 가중치가 부여된 데이터셋 시각화

Matplotlib 라이브러리를 사용하여 가중치가 부여된 데이터셋을 시각화합니다. 점의 크기는 해당 점의 가중치에 비례합니다.

```python
xx, yy = np.meshgrid(np.linspace(-4, 5, 500), np.linspace(-4, 5, 500))
fig, ax = plt.subplots()
ax.scatter(
    X[:, 0],
    X[:, 1],
    c=y,
    s=sample_weight,
    alpha=0.9,
    cmap=plt.cm.bone,
    edgecolor="black",
)
```
