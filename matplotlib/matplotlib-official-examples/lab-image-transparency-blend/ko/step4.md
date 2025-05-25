# 투명도를 사용하여 값 강조

마지막으로, 동일한 플롯을 다시 만들지만 이번에는 투명도를 사용하여 데이터의 극단적인 값을 강조합니다. 이는 종종 p-값이 작은 데이터 포인트를 강조하는 데 사용됩니다. 또한 이미지 값을 강조하기 위해 등고선도 추가합니다.

```python
# 가중치 값을 기반으로 알파 채널을 생성합니다.
alphas = Normalize(0, .3, clip=True)(np.abs(weights))
alphas = np.clip(alphas, .4, 1)  # alpha value clipped at the bottom at .4

# 그림과 이미지를 생성합니다.
fig, ax = plt.subplots()
ax.imshow(greys)
ax.imshow(weights, alpha=alphas, **imshow_kwargs)

# 다른 레벨을 추가로 강조하기 위해 등고선을 추가합니다.
ax.contour(weights[::-1], levels=[-.1, .1], colors='k', linestyles='-')
ax.set_axis_off()
plt.show()

ax.contour(weights[::-1], levels=[-.0001, .0001], colors='k', linestyles='-')
ax.set_axis_off()
plt.show()
```
