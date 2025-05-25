# 컬러맵 반전

Matplotlib 는 컬러맵 이름에 `_r`을 추가하여 컬러맵을 반전시키는 기능을 제공합니다.

```python
import matplotlib.pyplot as plt

# 반전된 'viridis' 컬러맵을 사용하여 플롯 생성
plt.imshow(data, cmap='viridis_r')
plt.colorbar()
```
