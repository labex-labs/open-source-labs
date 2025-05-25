# 기본 Monospace 글꼴 선택

Matplotlib 의 기본 monospace 글꼴은 운영 체제에 의해 결정됩니다. `font.family` 매개변수를 `'monospace'`로 설정하여 기본 monospace 글꼴을 사용하도록 선택할 수 있습니다. 이를 위해 다음 코드를 사용할 수 있습니다.

```python
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "monospace"
```
