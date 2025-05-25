# 데이터 준비

차트에 사용할 데이터는 이 단계에서 준비됩니다. 사람들의 이름, 성과, 그리고 오차율의 목록을 생성합니다.

```python
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))
```
