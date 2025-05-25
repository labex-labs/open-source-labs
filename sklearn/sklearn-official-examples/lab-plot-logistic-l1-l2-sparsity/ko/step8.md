# 제목 및 레이블 설정

서브플롯의 제목과 레이블을 설정합니다.

```python
    if i == 0:
        axes_row[0].set_title("L1 페널티")
        axes_row[1].set_title("탄성 네트\nl1_ratio = %s" % l1_ratio)
        axes_row[2].set_title("L2 페널티")

    axes_row[0].set_ylabel("C = %s" % C)
```
