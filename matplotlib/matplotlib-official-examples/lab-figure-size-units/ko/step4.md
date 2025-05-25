# 픽셀 단위의 그림 크기

그림 크기를 픽셀 단위로 지정할 수도 있습니다. 이렇게 하려면 픽셀 값을 인치로 변환해야 합니다. 픽셀에서 인치로의 변환 계수는 dpi (dots per inch, 인치당 점) 값으로 1 을 나누어 얻을 수 있습니다. 그런 다음 이 값을 subplots 함수의 figsize 매개변수로 사용할 수 있습니다. 아래 코드는 600 픽셀 x 200 픽셀 크기의 그림을 만드는 방법을 보여줍니다.

```python
px = 1/plt.rcParams['figure.dpi']  # pixel in inches
plt.subplots(figsize=(600*px, 200*px))
plt.show()
```
