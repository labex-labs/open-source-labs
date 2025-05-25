# 파이 차트 (Pie Chart) 생성

Matplotlib 을 사용하여 파이 차트를 만들 수도 있습니다. 이 예제에서는 다양한 종류의 피자를 선호하는 사람들의 비율을 보여주는 파이 차트를 만들 것입니다.

```python
import matplotlib.pyplot as plt

# 플롯할 데이터
sizes = [30, 40, 10, 20]
labels = ["Pepperoni", "Mushroom", "Onion", "Sausage"]

# 파이 차트 생성
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# 제목 설정
plt.title("Simple Pie Chart")

# 플롯 표시
plt.show()
```
