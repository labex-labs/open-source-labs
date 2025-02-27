# Загрузка текстовых данных

Во - первых, нам нужно загрузить текстовые данные, с которыми мы будем работать. Мы будем использовать датасет 20 Newsgroups, который содержит новостные статьи по двадцати различным темам. Чтобы загрузить датасет, мы можем использовать функцию `fetch_20newsgroups` из scikit - learn.

```python
from sklearn.datasets import fetch_20newsgroups

# Load the dataset
categories = ['alt.atheism','soc.religion.christian', 'comp.graphics','sci.med']
twenty_train = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)
```

Теперь мы загрузили данные, и можем изучить их структуру и содержание.
