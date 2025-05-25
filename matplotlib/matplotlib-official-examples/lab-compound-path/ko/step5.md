# 플롯 생성

플롯을 생성하고 `PathPatch`를 플롯에 추가합니다. 플롯의 제목을 `'A Compound Path'`로 설정합니다.

```python
fig, ax = plt.subplots()
ax.add_patch(pathpatch)
ax.set_title('A Compound Path')

ax.autoscale_view()

plt.show()
```
