# 플롯 사용자 정의

이제 기본적인 플롯을 생성했으므로, 시각적으로 더 매력적으로 만들기 위해 사용자 정의해 보겠습니다. 제목, 축 레이블을 추가하고 선의 색상과 스타일을 변경할 수 있습니다.

```python
# Add title and axis labels
plt.title('Sin Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Change color and style of line
plt.plot(x, y, color='red', linestyle='dashed')
plt.show()
```
