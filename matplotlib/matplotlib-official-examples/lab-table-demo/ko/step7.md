# 플롯에 테이블 추가

`plt.table` 함수를 사용하여 플롯 하단에 테이블을 추가합니다. 셀 텍스트, 행 레이블, 행 색상 및 열 레이블을 함수의 매개변수로 전달합니다.

```python
the_table = plt.table(cellText=cell_text,
                      rowLabels=rows,
                      rowColours=colors,
                      colLabels=columns,
                      loc='bottom')
```
