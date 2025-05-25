# 내장 컬러맵 사용

Matplotlib 는 데이터를 표현하는 데 사용할 수 있는 다양한 내장 컬러맵을 제공합니다. 이러한 컬러맵은 `matplotlib.cm` 모듈에 나열된 이름을 사용하여 액세스할 수 있습니다.

```python
import matplotlib.pyplot as plt

# 'viridis' 컬러맵을 사용하여 플롯 생성
plt.imshow(data, cmap='viridis')
plt.colorbar()
```
