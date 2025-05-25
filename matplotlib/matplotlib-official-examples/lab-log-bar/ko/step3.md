# 막대 차트 생성

이제 막대 차트를 생성할 준비가 되었습니다. 먼저 막대의 너비와 x 축에서의 위치를 설정하는 데 도움이 되는 몇 가지 변수를 정의합니다.

```python
dim = len(data[0])
w = 0.75
dimw = w / dim
```

다음으로, `subplots()` 메서드를 사용하여 figure 와 axis 객체를 생성합니다. 그런 다음 for 루프를 사용하여 데이터 세트의 각 값을 반복하고 각 값에 대한 막대를 생성합니다.

```python
fig, ax = plt.subplots()
x = np.arange(len(data))
for i in range(len(data[0])):
    y = [d[i] for d in data]
    b = ax.bar(x + i * dimw, y, dimw, bottom=0.001)
```

`bottom` 매개변수를 `0.001`로 설정하여 높이가 0 인 막대가 없도록 합니다. 이는 로그 스케일과 호환되지 않습니다.
