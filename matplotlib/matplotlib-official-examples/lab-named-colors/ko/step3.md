# 간단한 플롯 생성

Matplotlib 을 가져왔으므로 이를 사용하여 간단한 플롯을 만들 수 있습니다. 이 예제에서는 x 값과 y 값 간의 관계를 보여주는 선 그래프 (line plot) 를 만들 것입니다.

```python
import matplotlib.pyplot as plt

# x-축 값
x = [1, 2, 3, 4, 5]

# y-축 값
y = [2, 4, 6, 8, 10]

# 선 그리기
plt.plot(x, y)

# 제목 설정
plt.title("Simple Line Plot")

# x-축 레이블 설정
plt.xlabel("X-axis")

# y-축 레이블 설정
plt.ylabel("Y-axis")

# 플롯 표시
plt.show()
```
