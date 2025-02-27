# データセットの読み込み

ここでは、20 のトピックに関する約 18,000 のニュースグループ投稿が含まれる 20 newsgroups データセットを使用します。このステップでは、データセットを読み込み、その基本情報をいくつか表示します。

```python
import numpy as np
from sklearn.datasets import fetch_20newsgroups

# 最初の 5 つのカテゴリでデータセットを読み込む
data = fetch_20newsgroups(
    subset="train",
    categories=[
        "alt.atheism",
        "comp.graphics",
        "comp.os.ms-windows.misc",
        "comp.sys.ibm.pc.hardware",
        "comp.sys.mac.hardware",
    ],
)

# データセットに関する情報を表示する
print("%d documents" % len(data.filenames))
print("%d categories" % len(data.target_names))
```
