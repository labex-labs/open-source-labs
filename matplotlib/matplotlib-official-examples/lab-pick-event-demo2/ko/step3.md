# 데이터 플롯

이제 Matplotlib 의 pyplot 모듈을 사용하여 mu 대 sigma 를 플롯합니다. mu 와 sigma 에 대해 계산된 값을 사용하여 산점도 (scatter plot) 를 생성합니다. 또한 `picker` 매개변수를 True 로 설정하여 플롯에 상호 작용성을 추가합니다.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_title('click on point to plot time series')
line, = ax.plot(xs, ys, 'o', picker=True, pickradius=5)
```
