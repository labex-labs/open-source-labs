# 서브플롯 생성

Matplotlib 의 `subplots` 함수를 사용하여 세 개의 서브플롯을 생성합니다. 서브플롯이 공통 x 축을 공유하도록 `sharex` 매개변수를 `True`로 설정합니다. 또한 `subplots_adjust` 함수를 사용하여 서브플롯 간의 수직 간격을 제거합니다.

```python
fig, axs = plt.subplots(3, 1, sharex=True)
fig.subplots_adjust(hspace=0)
```
