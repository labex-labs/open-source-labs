# 加载文本数据

首先，我们需要加载要处理的文本数据。我们将使用20新闻组数据集，其中包含来自二十个不同主题的新闻文章。要加载该数据集，我们可以使用scikit-learn中的`fetch_20newsgroups`函数。

```python
from sklearn.datasets import fetch_20newsgroups

# 加载数据集
categories = ['alt.atheism','soc.religion.christian', 'comp.graphics','sci.med']
twenty_train = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)
```

现在我们已经加载了数据，可以探索其结构和内容。
