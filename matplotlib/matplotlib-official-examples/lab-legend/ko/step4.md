# 범례 추가

플롯에 범례를 추가하기 위해 Matplotlib 의 `legend` 함수를 사용합니다. `loc` 매개변수를 전달하여 범례의 위치를 지정하고, `shadow` 매개변수를 사용하여 범례에 그림자 효과를 추가합니다. 또한 `fontsize` 매개변수를 사용하여 범례의 글꼴 크기를 설정합니다.

```python
legend = ax.legend(loc='upper center', shadow=True, fontsize='x-large')
```
