# 설정

시작하기 전에 Matplotlib 이 설치되었는지 확인해야 합니다. 다음 명령을 실행하여 pip 를 사용하여 설치할 수 있습니다.

```python
!pip install matplotlib
```

설치가 완료되면 라이브러리를 가져오고 환경을 설정해야 합니다.

```python
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

# Create new Figure with black background
fig = plt.figure(figsize=(8, 8), facecolor='black')

# Add a subplot with no frame
ax = plt.subplot(frameon=False)
```
