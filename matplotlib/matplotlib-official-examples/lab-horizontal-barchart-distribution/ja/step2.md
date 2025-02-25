# データの準備

カテゴリとアンケート結果を定義する必要があります。この例では、人々が5段階で質問に対する同意度を評価したアンケートがあります。カテゴリを `category_names` として、アンケート結果を `results` として定義します。

```python
category_names = ['Strongly disagree', 'Disagree',
                  'Neither agree nor disagree', 'Agree', 'Strongly agree']
results = {
    'Question 1': [10, 15, 17, 32, 26],
    'Question 2': [26, 22, 29, 10, 13],
    'Question 3': [35, 37, 7, 2, 19],
    'Question 4': [32, 11, 9, 15, 33],
    'Question 5': [21, 29, 5, 5, 40],
    'Question 6': [8, 19, 5, 30, 38]
}
```
