# 加载数据

我们将从 `20newsgroups_dataset` 加载数据，该数据集包含约18000篇关于20个主题的新闻组帖子，分为两个子集：一个用于训练，一个用于测试。为了简单起见并降低计算成本，我们选择7个主题的子集并仅使用训练集。

```python
from sklearn.datasets import fetch_20newsgroups

categories = [
    "alt.atheism",
    "comp.graphics",
    "comp.sys.ibm.pc.hardware",
    "misc.forsale",
    "rec.autos",
    "sci.space",
    "talk.religion.misc",
]

print("Loading 20 newsgroups training data")
raw_data, _ = fetch_20newsgroups(subset="train", categories=categories, return_X_y=True)
data_size_mb = sum(len(s.encode("utf-8")) for s in raw_data) / 1e6
print(f"{len(raw_data)} documents - {data_size_mb:.3f}MB")
```
