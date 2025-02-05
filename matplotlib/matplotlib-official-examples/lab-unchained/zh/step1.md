# 准备工作

在开始之前，我们需要确保已安装 Matplotlib。你可以使用 pip 通过运行以下命令来安装它：

```python
!pip install matplotlib
```

安装完成后，我们需要导入该库并设置环境：

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
