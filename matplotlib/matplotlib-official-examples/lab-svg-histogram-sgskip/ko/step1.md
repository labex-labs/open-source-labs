# 히스토그램, 범례 및 제목 생성

먼저, Matplotlib 을 사용하여 히스토그램, 범례 및 제목을 생성합니다. 또한 `set_gid()` 메서드를 사용하여 각 객체에 ID 를 할당합니다. 이는 Python 에서 생성된 Matplotlib 객체와 두 번째 단계에서 파싱되는 해당 SVG 구조를 연결하는 데 도움이 됩니다.

```python
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

# Create histogram, legend, and title
plt.figure()
r = np.random.randn(100)
r1 = r + 1
labels = ['Rabbits', 'Frogs']
H = plt.hist([r, r1], label=labels)
containers = H[-1]
leg = plt.legend(frameon=False)
plt.title("From a web browser, click on the legend\n"
          "marker to toggle the corresponding histogram.")

# Assign IDs to the SVG objects we'll modify
hist_patches = {}
for ic, c in enumerate(containers):
    hist_patches[f'hist_{ic}'] = []
    for il, element in enumerate(c):
        element.set_gid(f'hist_{ic}_patch_{il}')
        hist_patches[f'hist_{ic}'].append(f'hist_{ic}_patch_{il}')

# Set IDs for the legend patches
for i, t in enumerate(leg.get_patches()):
    t.set_gid(f'leg_patch_{i}')

# Set IDs for the text patches
for i, t in enumerate(leg.get_texts()):
    t.set_gid(f'leg_text_{i}')
```
