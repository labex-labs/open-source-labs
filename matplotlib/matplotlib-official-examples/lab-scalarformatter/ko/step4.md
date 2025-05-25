# 서브플롯에 데이터 플롯

3 단계에서 생성한 서브플롯에 생성된 데이터를 플롯합니다.

```python
for col in axs.T:
    col[0].plot(plot1_x, plot1_y)
    col[1].plot(plot2_x, plot2_y)
    col[2].plot(plot3_x, plot3_y)
```
