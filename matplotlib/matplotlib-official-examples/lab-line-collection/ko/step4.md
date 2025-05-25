# 플롯 생성

이제 `matplotlib`를 사용하여 플롯을 생성하고, `Axes` 객체의 `add_collection` 메서드를 사용하여 `LineCollection` 객체를 플롯에 추가할 수 있습니다.

```python
fig, ax = plt.subplots()
ax.set_xlim(x.min(), x.max())
ax.set_ylim(ys.min(), ys.max())

ax.add_collection(line_segments)
ax.set_title('Masked arrays 를 사용한 Line collection')
plt.show()
```
