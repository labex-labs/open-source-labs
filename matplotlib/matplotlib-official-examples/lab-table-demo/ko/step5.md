# 수직 누적 막대 차트 생성

`plt.bar` 함수를 사용하여 연도별 다양한 자연 재해로 인한 손실을 나타내는 수직 누적 막대 차트 (vertical stacked bar chart) 를 생성합니다. for 루프를 사용하여 각 데이터 행을 반복하고 막대를 플롯합니다.

```python
n_rows = len(data)

index = np.arange(len(columns)) + 0.3
bar_width = 0.4

y_offset = np.zeros(len(columns))

cell_text = []
for row in range(n_rows):
    plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
    y_offset = y_offset + data[row]
    cell_text.append(['%1.1f' % (x / 1000.0) for x in y_offset])
```
