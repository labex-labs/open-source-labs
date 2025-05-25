# `ax.pie`를 사용하여 중첩 파이 차트 만들기

`ax.pie` 메서드를 사용하여 중첩 파이 차트를 만들 수 있습니다. 먼저 세 그룹에 해당하는 가짜 데이터를 생성합니다. 내부 원에서는 각 숫자를 자체 그룹에 속하는 것으로 처리합니다. 외부 원에서는 원래 3 개 그룹의 구성원으로 플롯합니다.

```python
fig, ax = plt.subplots()

size = 0.3
vals = np.array([[60., 32.], [37., 40.], [29., 10.]])

cmap = plt.colormaps["tab20c"]
outer_colors = cmap(np.arange(3)*4)
inner_colors = cmap([1, 2, 5, 6, 9, 10])

ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors,
       wedgeprops=dict(width=size, edgecolor='w'))

ax.pie(vals.flatten(), radius=1-size, colors=inner_colors,
       wedgeprops=dict(width=size, edgecolor='w'))

ax.set(aspect="equal", title='Pie plot with `ax.pie`')
plt.show()
```
