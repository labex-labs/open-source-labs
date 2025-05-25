# 차트 사용자 정의

축 레이블과 제목을 추가하여 차트를 더 사용자 정의할 수 있습니다. 또한 축 레이블과 범례 제목의 색상을 변경할 수 있습니다. 다음 코드는 차트를 사용자 정의하는 방법을 보여줍니다.

```python
fig, ax = plt.subplots()
ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
ax.set_ylabel('fruit supply', color='blue')
ax.set_xlabel('fruit names', color='blue')
ax.set_title('Fruit supply by kind and color', color='purple')
ax.legend(title='Fruit color', title_color='red', labelcolor='green')
plt.show()
```
