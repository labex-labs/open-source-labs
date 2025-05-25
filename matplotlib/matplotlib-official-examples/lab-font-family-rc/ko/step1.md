# 기본 Sans-Serif 글꼴 선택

Matplotlib 의 기본 글꼴 패밀리는 sans-serif 입니다. `font.family` 매개변수를 `'sans-serif'`로 설정하여 기본 글꼴 패밀리를 사용하도록 선택할 수 있습니다. 이를 위해 다음 코드를 사용할 수 있습니다.

```python
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "sans-serif"
```
