# Dataset

We will use the 20 newsgroups dataset, which consists of posts from newsgroups on 20 topics. The dataset is split into train and test subsets based on messages posted before and after a specific date. We will only use posts from 2 categories to speed up running time.

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


