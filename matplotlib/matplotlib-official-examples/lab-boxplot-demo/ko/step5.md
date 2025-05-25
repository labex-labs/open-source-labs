# 레이블 및 제목 추가

마지막으로, 상자 그림에 레이블과 제목을 추가하여 더 많은 정보를 제공할 수 있습니다. x 축과 y 축에 레이블을 추가하고, 플롯에 제목을 추가할 수 있습니다. 또한 레이블과 제목의 글꼴 크기와 스타일을 변경할 수 있습니다. 다음은 레이블과 제목을 추가하는 예입니다.

```python
plt.boxplot([data1, data2, data3])
plt.xlabel('Group')
plt.ylabel('Value')
plt.title('Comparison of Three Groups')
plt.xticks([1, 2, 3], ['Group 1', 'Group 2', 'Group 3'])
plt.show()
```
