# 必要なモジュールをインポートする

まず最初に、グラフを作成するために必要なモジュールをインポートします。x と y のデータを生成するために`numpy`を、グラフを作成するために`matplotlib.pyplot`を、2 番目の y 軸を作成するために`mpl_toolkits.axes_grid1`を使用します。

```python
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import host_subplot
```
