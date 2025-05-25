# 데이터 타입 확인

첫 번째 단계는 x 축 값의 데이터 타입을 확인하는 것입니다. 문자열 목록인 경우, 눈금 동작이 예상과 다를 가능성이 높습니다. 이를 해결하려면 문자열을 숫자형으로 변환해야 합니다. 다음은 예시입니다.

```python
import matplotlib.pyplot as plt
import numpy as np

# create example data
x = ['1', '5', '2', '3']
y = [1, 4, 2, 3]

# plot the data with string tick labels
fig, ax = plt.subplots()
ax.plot(x, y, 'd')
ax.set_xlabel('Categories')
plt.show()
```

이 예제에서는 x 축에 문자열 목록이 있습니다. 데이터를 플롯하면 눈금 레이블이 순서대로 표시되지 않고 잘못 배치됩니다.
