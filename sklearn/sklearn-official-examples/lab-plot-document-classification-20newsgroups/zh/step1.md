# 加载并向量化20新闻组文本数据集

我们定义一个函数来从20新闻组数据集中加载数据，该数据集包含约18,000篇关于20个主题的新闻组帖子，分为两个子集：一个用于训练，另一个用于测试。我们将在不剥离元数据的情况下加载并向量化数据集。

```python
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer

categories = [
    "alt.atheism",
    "talk.religion.misc",
    "comp.graphics",
    "sci.space",
]

def load_dataset(verbose=False, remove=()):
    """加载并向量化20新闻组数据集。"""
    data_train = fetch_20newsgroups(
        subset="train",
        categories=categories,
        shuffle=True,
        random_state=42,
        remove=remove,
    )

    data_test = fetch_20newsgroups(
        subset="test",
        categories=categories,
        shuffle=True,
        random_state=42,
        remove=remove,
    )

    # `target_names` 中标签的顺序可能与 `categories` 不同
    target_names = data_train.target_names

    # 将目标拆分为训练集和测试集
    y_train, y_test = data_train.target, data_test.target

    # 使用稀疏向量化器从训练数据中提取特征
    vectorizer = TfidfVectorizer(
        sublinear_tf=True, max_df=0.5, min_df=5, stop_words="english"
    )
    X_train = vectorizer.fit_transform(data_train.data)

    # 使用相同的向量化器从测试数据中提取特征
    X_test = vectorizer.transform(data_test.data)

    feature_names = vectorizer.get_feature_names_out()

    if verbose:
        print(f"{len(data_train.data)} 个文档")
        print(f"{len(data_test.data)} 个文档")
        print(f"{len(target_names)} 个类别")
        print(f"样本数: {X_train.shape[0]}, 特征数: {X_train.shape[1]}")
        print(f"样本数: {X_test.shape[0]}, 特征数: {X_test.shape[1]}")

    return X_train, X_test, y_train, y_test, feature_names, target_names

X_train, X_test, y_train, y_test, feature_names, target_names = load_dataset(verbose=True)
```
