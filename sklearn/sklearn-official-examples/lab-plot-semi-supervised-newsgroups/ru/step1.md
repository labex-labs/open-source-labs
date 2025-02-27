# Загрузка набора данных

Мы будем использовать набор данных 20 newsgroups, который содержит около 18 000 постов из новостных групп по 20 темам. На этом шаге мы загрузим набор данных и выведем основную информацию о нем.

```python
import numpy as np
from sklearn.datasets import fetch_20newsgroups

# Загрузка набора данных с первыми пятью категориями
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

# Вывод информации о наборе данных
print("%d documents" % len(data.filenames))
print("%d categories" % len(data.target_names))
```
