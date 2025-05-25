# 색상 사용자 정의

`pie()` 함수의 `colors` 매개변수에 색상 리스트를 전달하여 슬라이스의 색상을 사용자 정의할 수 있습니다.

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=['olivedrab', 'rosybrown', 'gray', 'saddlebrown'])
```
