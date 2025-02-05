# 加载数据集

我们将使用20新闻组数据集，该数据集包含约18,000篇关于20个主题的新闻组文章。在这一步中，我们将加载数据集并打印出有关它的一些基本信息。

```python
import numpy as np
from sklearn.datasets import fetch_20newsgroups

# 加载前五个类别的数据集
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

# 打印有关数据集的信息
print("%d documents" % len(data.filenames))
print("%d categories" % len(data.target_names))
```
