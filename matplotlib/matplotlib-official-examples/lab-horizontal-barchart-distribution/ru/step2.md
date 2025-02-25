# Подготовка данных

Нам необходимо определить категории и результаты опроса. В этом примере у нас есть опрос, в котором люди оценивали свою согласованность с вопросами по пятибалльной шкале. Мы определим категории как `category_names`, а результаты опроса как `results`.

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
