# 문자열을 숫자형으로 변환

눈금 동작을 수정하려면 문자열을 숫자형으로 변환해야 합니다. 다음은 예시입니다.

```python
import matplotlib.pyplot as plt
import numpy as np

# create example data
x = ['1', '5', '2', '3']
y = [1, 4, 2, 3]

# convert strings to floats
x = np.asarray(x, dtype='float')

# plot the data with numeric tick labels
fig, ax = plt.subplots()
ax.plot(x, y, 'd')
ax.set_xlabel('Floats')
plt.show()
```

이 예제에서는 `np.asarray()`를 사용하여 문자열 값을 float 로 변환합니다. 데이터를 다시 플롯하면 눈금 레이블이 예상대로 표시됩니다.
