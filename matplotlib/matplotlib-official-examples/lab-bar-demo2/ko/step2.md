# 막대 그래프를 위한 데이터 생성

이 단계에서는 막대 그래프를 위한 데이터를 생성해야 합니다. numpy 라이브러리를 사용하여 막대 그래프에 사용할 값의 배열을 생성합니다.

```python
from basic_units import cm, inch

cms = cm * np.arange(0, 10, 2)
bottom = 0 * cm
width = 0.8 * cm
```
