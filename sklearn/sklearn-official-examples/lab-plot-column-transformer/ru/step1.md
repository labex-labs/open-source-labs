# Набор данных

Мы будем использовать набор данных 20 newsgroups, который состоит из сообщений из новостных групп по 20 темам. Набор данных разделен на обучающую и тестовую подмножества в зависимости от сообщений, опубликованных до и после определенной даты. Мы будем использовать только сообщения из 2 категорий, чтобы ускорить время выполнения.

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
