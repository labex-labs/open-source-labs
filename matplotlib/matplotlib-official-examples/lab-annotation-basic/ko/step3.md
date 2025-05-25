# 플롯 주석 추가

이제 특정 좌표를 가리키는 화살표를 추가하여 플롯에 주석을 추가합니다. 이 예제에서는 코사인 함수의 국소 최댓값을 가리키는 화살표를 추가합니다.

```python
ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
```

`ax.annotate()` 함수는 여러 인수를 받습니다. 첫 번째 인수는 플롯에 표시될 텍스트입니다. `xy` 인수는 주석을 추가하려는 점의 좌표를 지정합니다. `xytext` 인수는 텍스트의 좌표를 지정합니다. `arrowprops` 인수는 화살표의 속성을 지정하는 딕셔너리입니다.
