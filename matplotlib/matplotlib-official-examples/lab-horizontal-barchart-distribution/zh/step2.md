# 准备数据

我们需要定义类别和调查结果。在这个例子中，我们有一项调查，人们在一个五级量表上对问题的同意程度进行评分。我们将把类别定义为 `category_names`，把调查结果定义为 `results`。

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
