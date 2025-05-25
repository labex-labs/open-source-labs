# 플롯 사용자 정의

이제 기본적인 플롯이 있으므로 이를 사용자 정의해 보겠습니다.

```python
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, color='red', marker='o')
plt.title('My Plot')
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.show()
```

여기서는 플롯에 몇 가지 사용자 정의를 추가했습니다. 선의 색상을 빨간색으로 변경하고 각 데이터 포인트에 원형 마커를 추가했습니다. 또한 플롯에 제목과 축 레이블을 추가했습니다.
