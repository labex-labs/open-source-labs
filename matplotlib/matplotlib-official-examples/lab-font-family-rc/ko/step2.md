# 특정 Sans-Serif 글꼴 선택

특정 sans-serif 글꼴을 사용하려면 `font.sans-serif` 매개변수를 글꼴 이름 목록으로 설정할 수 있습니다. Matplotlib 는 사용자의 시스템에서 사용 가능한 목록의 첫 번째 글꼴을 사용하려고 시도합니다. 이를 위해 다음 코드를 사용할 수 있습니다.

```python
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Nimbus Sans"]
```
