# Matplotlib 임포트 및 산점도 생성

Matplotlib 를 임포트하고 산점도 (scatter plot) 를 생성하는 것으로 시작합니다.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

sc = ax.scatter([1, 2], [1, 2], c=[1, 2])
```
