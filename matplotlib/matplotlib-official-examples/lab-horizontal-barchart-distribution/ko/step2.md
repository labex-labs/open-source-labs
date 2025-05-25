# 데이터 준비

범주와 설문 조사 결과를 정의해야 합니다. 이 예제에서는 사람들이 5 점 척도로 질문에 대한 동의 정도를 평가하는 설문 조사가 있습니다. 범주는 `category_names`로, 설문 조사 결과는 `results`로 정의합니다.

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
