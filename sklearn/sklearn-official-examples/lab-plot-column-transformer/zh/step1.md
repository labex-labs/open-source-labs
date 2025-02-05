# 数据集

我们将使用20个新闻组数据集，该数据集由20个主题的新闻组帖子组成。根据特定日期之前和之后发布的消息，数据集被分为训练集和测试子集。为了加快运行速度，我们将只使用来自2个类别的帖子。

```python
categories = ["sci.med", "sci.space"]
X_train, y_train = fetch_20newsgroups(
    random_state=1,
    subset="train",
    categories=categories,
    remove=("footers", "quotes"),
    return_X_y=True,
)
X_test, y_test = fetch_20newsgroups(
    random_state=1,
    subset="test",
    categories=categories,
    remove=("footers", "quotes"),
    return_X_y=True,
)
```
