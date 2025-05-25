# 막대 그래프 (Bar Plot) 생성

Matplotlib 을 사용하여 막대 그래프를 만들 수도 있습니다. 이 예제에서는 판매된 사과, 바나나, 오렌지의 수를 보여주는 막대 그래프를 만들 것입니다.

```python
import matplotlib.pyplot as plt

# 플롯할 데이터
apples = 10
bananas = 15
oranges = 5

# 막대 그래프 생성
plt.bar(["Apples", "Bananas", "Oranges"], [apples, bananas, oranges])

# 제목 설정
plt.title("Simple Bar Plot")

# x-축 레이블 설정
plt.xlabel("Fruits")

# y-축 레이블 설정
plt.ylabel("Quantity")

# 플롯 표시
plt.show()
```
