# 첫 번째 서브플롯에 데이터 플롯

matplotlib.pyplot 의 plot 함수를 사용하여 첫 번째 서브플롯에 x 값의 코사인 (cosine) 을 플롯합니다. x 축이 라디안 (radians) 단위임을 지정하기 위해 xunits 매개변수를 사용합니다.

```python
from basic_units import cos
axs[0].plot(x, cos(x), xunits=radians)
```
