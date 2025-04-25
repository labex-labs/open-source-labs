# セットアップ

始める前に、Matplotlib がインストールされていることを確認する必要があります。pip を使って、次のコマンドを実行することでインストールできます。

```python
!pip install matplotlib
```

インストールが完了したら、ライブラリをインポートして環境をセットアップする必要があります。

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
