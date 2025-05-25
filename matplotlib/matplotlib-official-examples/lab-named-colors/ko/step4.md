# 산점도 (Scatter Plot) 생성

Matplotlib 을 사용하여 산점도를 만들 수도 있습니다. 이 예제에서는 x 값과 y 값 간의 관계를 보여주는 산점도를 만들 것입니다.

```python
import matplotlib.pyplot as plt

# x-축 값
x = [1, 2, 3, 4, 5]

# y-축 값
y = [2, 4, 6, 8, 10]

# 점 그리기
plt.scatter(x, y)

# 제목 설정
plt.title("Simple Scatter Plot")

# x-축 레이블 설정
plt.xlabel("X-axis")

# y-축 레이블 설정
plt.ylabel("Y-axis")

# 플롯 표시
plt.show()
```
