# 런타임에 rcParams 설정하기

Python 스크립트 내에서 또는 Python 셸에서 대화식으로 기본 런타임 구성 설정을 동적으로 변경할 수 있습니다. `matplotlib.rcParams` 변수는 Matplotlib 패키지에 전역적이며 모든 rc 설정을 저장합니다. 런타임에 rcParams 를 사용자 정의하려면 `mpl.rcParams` 딕셔너리를 사용하여 직접 수정할 수 있습니다. 다음은 예시입니다.

```python
import matplotlib as mpl

mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = '--'
```

이 코드는 Matplotlib 으로 생성된 모든 플롯에 대한 기본 선 너비와 선 스타일을 변경합니다.

새로운 기본 설정으로 플롯된 임의의 데이터를 살펴보겠습니다.

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = '--'
data = np.random.randn(50)
plt.plot(data)
plt.show()
```
