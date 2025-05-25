# 차트 사용자 정의

차트를 더 유익하게 만들기 위해 레이블, 제목을 추가하고 y 축을 반전시켜 사용자 정의할 수 있습니다.

```python
ax.set_yticks(y_pos, labels=people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')
```
