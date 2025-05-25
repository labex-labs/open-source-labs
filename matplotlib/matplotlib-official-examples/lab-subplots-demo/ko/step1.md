# 단일 서브플롯이 있는 그림 생성

단일 서브플롯을 생성하는 가장 간단한 방법은 인자 없이 `subplots()` 함수를 사용하는 것입니다. 이 함수는 `Figure` 객체와 단일 `Axes` 객체를 반환합니다.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
```
