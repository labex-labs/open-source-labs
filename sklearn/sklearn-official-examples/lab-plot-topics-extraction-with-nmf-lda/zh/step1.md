# 加载数据集

我们将加载 20 个新闻组数据集并对其进行向量化。我们使用一些启发式方法尽早过滤掉无用的术语：去除帖子的标题、页脚和引用的回复，并删除常见的英语单词、仅出现在一篇文档中或至少出现在 95% 的文档中的单词。

```python
from sklearn.datasets import fetch_20newsgroups

n_samples = 2000
n_features = 1000

print("Loading dataset...")
data, _ = fetch_20newsgroups(
    shuffle=True,
    random_state=1,
    remove=("headers", "footers", "quotes"),
    return_X_y=True,
)
data_samples = data[:n_samples]
```
