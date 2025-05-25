# 값을 색상에 매핑

`ScalarMappable.set_array` 함수를 사용하여 값의 배열을 색상에 매핑할 수도 있습니다. 새로운 데이터 세트와 `array` 매개변수를 `x` 값으로 설정한 새로운 `LineCollection` 객체를 생성합니다. 그런 다음 `Figure` 객체의 `colorbar` 메서드를 사용하여 플롯에 colorbar 를 추가할 수 있습니다.

```python
N = 50
x = np.arange(N)
ys = [x + i for i in x]
segs = [np.column_stack([x, y]) for y in ys]

fig, ax = plt.subplots()
ax.set_xlim(np.min(x), np.max(x))
ax.set_ylim(np.min(ys), np.max(ys))

line_segments = LineCollection(segs, array=x,
                               linewidths=(0.5, 1, 1.5, 2),
                               linestyles='solid')
ax.add_collection(line_segments)
axcb = fig.colorbar(line_segments)
axcb.set_label('Line Number')
ax.set_title('매핑된 색상을 사용한 Line Collection')
plt.sci(line_segments)
plt.show()
```
