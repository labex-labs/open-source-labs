# DateTime 눈금 처리

x 축에서 datetime 값을 사용할 때는 적절한 날짜 로케이터 (locator) 와 포맷터 (formatter) 를 얻기 위해 문자열을 datetime 객체로 변환하는 것이 중요합니다. 다음은 예시입니다.

```python
import matplotlib.pyplot as plt
import numpy as np

# create example data with datetime strings
x = ['2021-10-01', '2021-11-02', '2021-12-03', '2021-09-01']
y = [0, 2, 3, 1]

# convert strings to datetime64
x = np.asarray(x, dtype='datetime64[s]')

# plot the data with datetime tick labels
fig, ax = plt.subplots()
ax.plot(x, y, 'd')
ax.tick_params(axis='x', labelrotation=90)
plt.show()
```

이 예제에서는 `np.asarray()`를 사용하여 문자열 값을 datetime64 로 변환합니다. 데이터를 다시 플롯하면 눈금 레이블이 예상대로 표시됩니다.
