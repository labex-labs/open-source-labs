# 간단한 선택, 선, 사각형 및 텍스트

아티스트의 "picker" 속성을 설정하여 간단한 선택을 활성화하는 것으로 시작합니다. 이렇게 하면 마우스 이벤트가 아티스트 위에 있는 경우 아티스트가 선택 이벤트를 발생시킬 수 있습니다. 선, 사각형 및 텍스트를 포함하는 간단한 플롯을 만들고 각 아티스트에서 선택을 활성화합니다.

```python
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.set_title('click on points, rectangles or text', picker=True)
ax1.set_ylabel('ylabel', picker=True, bbox=dict(facecolor='red'))
line, = ax1.plot(rand(100), 'o', picker=True, pickradius=5)

# Pick the rectangle.
ax2.bar(range(10), rand(10), picker=True)
for label in ax2.get_xticklabels():  # Make the xtick labels pickable.
    label.set_picker(True)
```
