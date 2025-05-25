# 차원 정의

각 변의 길이에 대한 세 개의 변수, 즉 Nx, Ny 및 Nz 를 생성하여 상자의 차원을 정의합니다. 그런 다음 numpy 의 arange 메서드를 사용하여 X, Y 및 Z 에 대한 세 개의 메쉬 그리드를 생성합니다. 마지막으로, 평면 대신 상자를 생성하기 위해 Z 에 음수 값을 설정합니다.

```python
import matplotlib.pyplot as plt
import numpy as np

# Define dimensions
Nx, Ny, Nz = 100, 300, 500
X, Y, Z = np.meshgrid(np.arange(Nx), np.arange(Ny), -np.arange(Nz))
```
