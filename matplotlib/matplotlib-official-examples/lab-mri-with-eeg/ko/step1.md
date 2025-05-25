# MRI 데이터 로드 및 이미지 표시

첫 번째 단계는 MRI 데이터를 로드하고 이미지를 표시하는 것입니다. `imshow()` 함수를 사용하여 이미지를 표시하고, `axis('off')`를 사용하여 축 레이블을 제거합니다.

```python
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure("MRI_with_EEG")

# Load the MRI data (256x256 16-bit integers)
im = np.load('mri_data.npy')

# Plot the MRI image
ax0 = fig.add_subplot(2, 2, 1)
ax0.imshow(im, cmap='gray')
ax0.axis('off')
```
