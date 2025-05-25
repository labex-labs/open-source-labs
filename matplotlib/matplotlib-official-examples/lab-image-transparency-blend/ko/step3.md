# 투명도 혼합

`imshow`로 데이터를 플롯할 때 투명도를 포함하는 가장 간단한 방법은 데이터의 모양과 일치하는 배열을 `alpha` 인수에 전달하는 것입니다.

```python
# 오른쪽으로 이동하면서 선형적으로 증가하는 값의 알파 채널을 생성합니다.
alphas = np.ones(weights.shape)
alphas[:, 30:] = np.linspace(1, 0, 70)

# 그림과 이미지를 생성합니다.
fig, ax = plt.subplots()
ax.imshow(greys)
ax.imshow(weights, alpha=alphas, **imshow_kwargs)
ax.set_axis_off()
plt.show()
```
