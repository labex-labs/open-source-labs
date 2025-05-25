# 사용자 정의 figure 서브클래스를 사용하여 데이터 플롯

`plt.figure()` 함수를 사용하여 사용자 정의 figure 서브클래스 `WatermarkFigure`를 사용하여 데이터를 플롯합니다. 이 예제에서는 "draft" 워터마크 텍스트를 플롯에 추가합니다.

```python
plt.figure(FigureClass=WatermarkFigure, watermark='draft')
plt.plot(x, y)
```
