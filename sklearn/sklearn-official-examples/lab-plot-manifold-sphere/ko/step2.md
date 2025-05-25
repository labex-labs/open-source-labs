# 구형 데이터셋 생성

다음으로 구형 데이터셋을 생성합니다. 구를 만들고 극을 잘라내고 측면에 얇은 조각을 만듭니다. 이렇게 하면 다양체 학습 기법이 2 차원으로 투영하면서 '펼쳐낼' 수 있도록 합니다.

```python
n_neighbors = 10
n_samples = 1000

random_state = check_random_state(0)
p = random_state.rand(n_samples) * (2 * np.pi - 0.55)
t = random_state.rand(n_samples) * np.pi

indices = (t < (np.pi - (np.pi / 8))) & (t > ((np.pi / 8)))
colors = p[indices]
x, y, z = (
    np.sin(t[indices]) * np.cos(p[indices]),
    np.sin(t[indices]) * np.sin(p[indices]),
    np.cos(t[indices]),
)

fig = plt.figure(figsize=(15, 8))
plt.suptitle(
    "Manifold Learning with %i points, %i neighbors" % (1000, n_neighbors), fontsize=14
)

ax = fig.add_subplot(251, projection="3d")
ax.scatter(x, y, z, c=p[indices], cmap=plt.cm.rainbow)
ax.view_init(40, -10)

sphere_data = np.array([x, y, z]).T
```
