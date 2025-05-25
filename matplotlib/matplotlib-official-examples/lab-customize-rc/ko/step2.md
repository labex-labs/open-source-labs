# 기본 매개변수 사용자 정의

특정 그림에 대한 기본 매개변수를 사용자 정의하려면 `rcParams.update()` 메서드를 다시 사용할 수 있습니다. 이번에는 해당 그림에 대해 설정하려는 매개변수 이름과 값의 딕셔너리를 전달합니다. 다음은 특정 그림에 대한 몇 가지 기본 매개변수를 설정하는 예입니다.

```python
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.weight": "bold",
    "xtick.major.size": 5,
    "xtick.major.pad": 7,
    "xtick.labelsize": 15,
    "grid.color": "0.5",
    "grid.linestyle": "-",
    "grid.linewidth": 5,
    "lines.linewidth": 2,
    "lines.color": "g",
})
```
